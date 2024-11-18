#!/usr/bin/env python3

import rospy
import tf.transformations
import tf2_ros
import tf
from fiducial_msgs.msg import FiducialTransformArray
from ired_aruco.msg import MPSPosition
from std_srvs.srv import SetBool, SetBoolResponse

tfBuffer = None
aruco_position_ = []
aruco_position_msg_ = MPSPosition()
aruco_position_msg_.number_found = 0
save_data_ = False

def savePosition(req):
    global save_data_
    if req.data:
        save_data_ = True
        return SetBoolResponse(True, "Position will save.")
    else:
        save_data_ = False
        return SetBoolResponse(False, "Position not save.")

def checkPoitioninList(list_, target_):
    for i, row in enumerate(list_):
        for j, value in enumerate(row):
            if value == target_:
                return (i, j)
    return None

def arucoDetect(msg):
    global aruco_position_, aruco_position_msg_, save_data_
    if not save_data_ :
        aruco_position_ = []
        aruco_position_msg_ = MPSPosition()
    aruco_detect_ = msg
    try:
        id_ = int(aruco_detect_.transforms[0].fiducial_id)
        frame_ = f"fiducial_{id_}"
        check_id_inlist_= any(id_ in row_ for row_ in aruco_position_)
        if not check_id_inlist_:
            aruco_position_.append([id_, 0.0, 0.0, 0.0, 0, False])
        tf_transform_ = arucoTransform(id_, frame_)
        if tf_transform_:
            list_position_ = checkPoitioninList(aruco_position_, tf_transform_[0])
            if not aruco_position_[list_position_[0]][5] and -0.34906585 <= tf_transform_[4] <= 0.34906585 and tf_transform_[5] < 1.7:
                aruco_position_[list_position_[0]][1] += tf_transform_[1]
                aruco_position_[list_position_[0]][2] += tf_transform_[2]
                aruco_position_[list_position_[0]][3] += tf_transform_[3]
                aruco_position_[list_position_[0]][4] += 1
            
            if aruco_position_[list_position_[0]][4] >= 10 and not aruco_position_[list_position_[0]][5]:
                aruco_position_[list_position_[0]][1] /= aruco_position_[list_position_[0]][4]
                aruco_position_[list_position_[0]][2] /= aruco_position_[list_position_[0]][4]
                aruco_position_[list_position_[0]][3] /= aruco_position_[list_position_[0]][4]
                aruco_position_[list_position_[0]][5] = True
                aruco_position_msg_.number_found += 1
                aruco_position_msg_.id.append(str(aruco_position_[list_position_[0]][0]))
                aruco_position_msg_.x.append(float(aruco_position_[list_position_[0]][1]))
                aruco_position_msg_.y.append(float(aruco_position_[list_position_[0]][2]))
                aruco_position_msg_.theta.append(float(aruco_position_[list_position_[0]][3]))
    except Exception:
        pass

def arucoTransform(id_, frame_):
    global tfBuffer
    try:
        trans_ = tfBuffer.lookup_transform('aruco_camera_link', frame_, rospy.Time())
        x_ = trans_.transform.translation.x
        y_ = trans_.transform.translation.y
        tf_theta_ = tf.transformations.euler_from_quaternion([trans_.transform.rotation.x, trans_.transform.rotation.y, trans_.transform.rotation.z, trans_.transform.rotation.w])
        theta_ = tf_theta_[2] - 1.570796326794897
        if theta_ < -3.141592653589793:
            theta_ += (3.141592653589793*2)
        elif theta_ > 3.141592653589793:
            theta_ -= (3.141592653589793*2)
            
        trans_ = tfBuffer.lookup_transform('aruco_camera_link', frame_, rospy.Time())
        camera_dist_ = trans_.transform.translation.z
        tf_theta_ = tf.transformations.euler_from_quaternion([trans_.transform.rotation.x, trans_.transform.rotation.y, trans_.transform.rotation.z, trans_.transform.rotation.w])
        camera_theta_ = tf_theta_[1]

        return (id_, x_, y_, theta_, camera_theta_, camera_dist_)
    
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        pass

def main():
    global tfBuffer, aruco_position_msg_
    rospy.init_node('aruco_tf_node')
    rate = rospy.Rate(30)
    
    # Transform 
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    
    # Topic
    aruco_sub_ = rospy.Subscriber("/fiducial_transforms", FiducialTransformArray, arucoDetect)
    rospy.loginfo('Aruco detect position subscribe on /fiducial_transforms [fiducial_msgs/FiducialTransformArray]')
    
    aruco_position_pub_ = rospy.Publisher("/aruco_mps_explored", MPSPosition, queue_size=10)
    rospy.loginfo('Aruco position publish on /aruco_mps_explored [ired_msgs/MPSPosition]')
    
    # Service
    save_position_ = rospy.Service('/save_position_service', SetBool, savePosition)
    rospy.loginfo('Aruco save position service on /save_position_service [std_srvs/SetBool]')
 
    while not rospy.is_shutdown():
        aruco_position_pub_.publish(aruco_position_msg_)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException():
        pass
