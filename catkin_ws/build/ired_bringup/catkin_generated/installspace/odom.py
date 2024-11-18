#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, TransformStamped
from ired_msgs.msg import IMUData, MotorData
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState
import tf
import math
import numpy as np

# Global variables for sensor data
imu_ = IMUData()
joint_states_ = JointState()
motor_ = MotorData()
odom_ = Odometry()
odom_tf_ = TransformStamped()
robot_speed_ = Twist()
last_velocity_ = [0.0, 0.0, 0.0, 0.0]
last_position_ = [0.0, 0.0, 0.0, 0.0]
tf_broadcaster_ = tf.TransformBroadcaster()

wheel_radius = 0.065  # meters
robot_radius = 0.215  # meters

def IMUDataCallback(msg):
    global imu_
    imu_ = msg

def motorDataCallback(msg):
    global motor_
    motor_ = msg

def robotSpeedCallback(msg):
    global robot_speed_
    robot_speed_ = msg

def initData():
    global joint_states_, odom_
    joint_states_.name = ["wheel_front_left_joint", "wheel_front_right_joint", "wheel_rear_left_joint", "wheel_rear_right_joint"]
    joint_states_.header.frame_id = "base_footprint"
    joint_states_.position = [0.0, 0.0, 0.0, 0.0]
    joint_states_.velocity = [0.0, 0.0, 0.0, 0.0]
    joint_states_.effort = []
    odom_.child_frame_id = "base_footprint"
    odom_.header.frame_id = "odom"

def updateOdometry(diff_time):
    global imu_, motor_, odom_, robot_speed_, last_velocity_, last_position_
    
    theta_ = imu_.yaw
    dt = diff_time.to_sec()

    # Update odometry position
    delta_x_ = (robot_speed_.linear.x * math.cos(theta_) - robot_speed_.linear.y * math.sin(theta_)) * dt
    delta_y_ = (robot_speed_.linear.x * math.sin(theta_) + robot_speed_.linear.y * math.cos(theta_)) * dt
    odom_.pose.pose.position.x += delta_x_
    odom_.pose.pose.position.y += delta_y_
    odom_.pose.pose.position.z = 0.0

    # Update odometry orientation
    quaternion_ = tf.transformations.quaternion_from_euler(0.0, 0.0, theta_)
    odom_.pose.pose.orientation.x = quaternion_[0]
    odom_.pose.pose.orientation.y = quaternion_[1]
    odom_.pose.pose.orientation.z = quaternion_[2]
    odom_.pose.pose.orientation.w = quaternion_[3]

    # Update velocities
    odom_.twist.twist = robot_speed_

    # Wheel velocities from motor feedback
    v1 = motor_.speed_fb[0] * (2 * math.pi / 60) * wheel_radius  # Convert RPM to m/s
    v2 = motor_.speed_fb[1] * (2 * math.pi / 60) * wheel_radius
    v3 = motor_.speed_fb[2] * (2 * math.pi / 60) * wheel_radius
    v4 = motor_.speed_fb[3] * (2 * math.pi / 60) * wheel_radius

    # Wheel angular velocities
    w1 = v1 / wheel_radius
    w2 = v2 / wheel_radius
    w3 = v3 / wheel_radius
    w4 = v4 / wheel_radius

    # Update wheel positions (integrate over time)
    last_velocity_ = [w1, w2, w3, w4]
    last_position_[0] += w1 * dt
    last_position_[1] += w2 * dt
    last_position_[2] += w3 * dt
    last_position_[3] += w4 * dt

def updateJointStates():
    global joint_states_, last_position_, last_velocity_
    if len(joint_states_.name) == len(last_position_) == len(last_velocity_):
        joint_states_.position = last_position_
        joint_states_.velocity = last_velocity_
    else:
        rospy.logwarn("Mismatch in JointState array lengths.")

def updateTF():
    global odom_, tf_broadcaster_
    tf_broadcaster_.sendTransform(
        (odom_.pose.pose.position.x, odom_.pose.pose.position.y, odom_.pose.pose.position.z),
        (odom_.pose.pose.orientation.x, odom_.pose.pose.orientation.y, odom_.pose.pose.orientation.z, odom_.pose.pose.orientation.w),
        odom_.header.stamp,
        odom_.child_frame_id,
        odom_.header.frame_id
    )

def main():
    rospy.init_node('odom_node')
    rate = rospy.Rate(10)
    rospy.wait_for_message('/ired/motor/data', MotorData)

    joint_states_pub_ = rospy.Publisher('/joint_states', JointState, queue_size=10)
    odom_pub_ = rospy.Publisher('/odom', Odometry, queue_size=10)

    rospy.Subscriber('/ired/motor/data', MotorData, motorDataCallback)
    rospy.Subscriber('/ired/rollpitchyaw', IMUData, IMUDataCallback)
    rospy.Subscriber('/ired/speed', Twist, robotSpeedCallback)

    initData()
    prev_update_time_ = rospy.Time.now()

    while not rospy.is_shutdown():
        time_now_ = rospy.Time.now()
        diff_time_ = time_now_ - prev_update_time_
        prev_update_time_ = time_now_

        updateOdometry(diff_time_)
        odom_.header.stamp = time_now_
        odom_pub_.publish(odom_)

        updateJointStates()
        joint_states_.header.stamp = time_now_
        joint_states_pub_.publish(joint_states_)

        updateTF()
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
