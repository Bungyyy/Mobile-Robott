#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from ired_msgs.msg import IMUData
from sensor_msgs.msg import Imu
import tf.transformations as tf

imu_data_ = Imu()
imu_raw_ = Twist()
rpy_ = IMUData()

def calculateIMU():
    global imu_raw_, imu_data_, rpy_
    quaternion_ = tf.quaternion_from_euler(rpy_.roll, rpy_.pitch, rpy_.yaw)
    imu_data_.orientation.x = quaternion_[0]
    imu_data_.orientation.y = quaternion_[1]
    imu_data_.orientation.z = quaternion_[2]
    imu_data_.orientation.w = quaternion_[3]
    imu_data_.angular_velocity.x = imu_raw_.angular.x * 0.01745329252
    imu_data_.angular_velocity.y = imu_raw_.angular.y * 0.01745329252
    imu_data_.angular_velocity.z = imu_raw_.angular.z * 0.01745329252
    imu_data_.linear_acceleration = imu_raw_.linear

def calculateRPY(diff_time):
    global imu_raw_, rpy_
    rpy_.roll += (imu_raw_.angular.x * diff_time) * 0.01745329252
    rpy_.pitch += (imu_raw_.angular.y * diff_time) * 0.01745329252
    rpy_.yaw += (imu_raw_.angular.z * diff_time) * 0.01745329252

def IMUDataCallback(msg):
    global imu_raw_
    imu_raw_ = msg

def main():
    global imu_data_, rpy_
    rospy.init_node('imu_node')
    rate = rospy.Rate(10)
    rospy.loginfo("Wait for microntroller...")
    rospy.wait_for_message('/ired/imu/raw', Twist)
    imu_data_pub_ = rospy.Publisher('/ired/imu/data', Imu, queue_size=10)
    rpy_pub_ = rospy.Publisher('/ired/rollpitchyaw', IMUData, queue_size=10)
    rospy.Subscriber('ired/imu/raw', Twist, IMUDataCallback)
    rospy.loginfo("ROS publisher on /ired/imu/data [sensor_msgs/Imu]")
    rospy.loginfo("ROS publisher on /ired/rollpitchyaw [ired_msgs/IMUData]")
    rospy.loginfo("ROS subscriber on /ired/imu/raw [geometry_msgs/Twist]")
    
    imu_data_.header.frame_id = "imu_link"
    last_time = rospy.Time.now()
    
    while not rospy.is_shutdown():
        time_now = rospy.Time.now()
        diff_time = (time_now - last_time).to_sec()
        last_time = time_now
        
        calculateRPY(diff_time)
        rpy_pub_.publish(rpy_)
        
        calculateIMU()
        imu_data_.header.stamp = time_now
        imu_data_pub_.publish(imu_data_)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass