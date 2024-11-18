#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from ired_msgs.msg import MotorSpeed, MotorData, MotorControl

motor_control_ = MotorControl()
motor_data_ = MotorData()
motor_speed_ = MotorSpeed()
robot_speed_ = Twist()

import math

import math

def forwardKinematics():
    global motor_speed_, robot_speed_
    wheel_radius = 0.065  # in meters (adjust to your wheel's radius)
    robot_radius = 0.215  # distance from center of robot to each wheel, adjust as needed
    w1,w2,w3,w4 = motor_speed_.speed
    robot_speed_.linear.x = (((w1)+(w2)-(w3)-(w4)) * 0.35355 * (2 *3.14 * wheel_radius / 60))
    robot_speed_.linear.y = (((w1)-(w2)+(w3)-(w4)) * 0.35355 * (2 *3.14 * wheel_radius / 60))
    robot_speed_.angular.z = (0.25/robot_radius) * (w1+w2+w3+w4) * (2 *3.14 * wheel_radius / 60)
    # -(((w1*-0.25/robot_radius)+(w2*-0.25/robot_radius)+(w3*-0.25/robot_radius)+(w4*-0.25/robot_radius)) * (2 *3.14 * wheel_radius / 60))
    
def motorData():
    global motor_speed_, motor_data_, motor_control_
    motor_data_.speed_fb = motor_speed_.speed
    motor_data_.speed_sp = motor_control_.speed
    motor_data_.pid_motor_front_left = motor_control_.pid_motor_front_left
    motor_data_.pid_motor_front_right = motor_control_.pid_motor_front_right
    motor_data_.pid_motor_rear_left = motor_control_.pid_motor_rear_left
    motor_data_.pid_motor_rear_right = motor_control_.pid_motor_rear_right
    
def motorSpeedCallback(msg):
    global motor_speed_
    motor_speed_ = msg
    
def motorControlCallback(msg):
    global motor_control_
    motor_control_ = msg

def main():
    rospy.init_node('forward_kinematics_node')
    rate = rospy.Rate(10)
    rospy.loginfo("Waiting for rosserial...")
    rospy.wait_for_message('/ired/motor/speed_fb', MotorSpeed)
    robot_speed_pub_ = rospy.Publisher('/ired/speed', Twist, queue_size=10)
    motor_data_pub_ = rospy.Publisher('/ired/motor/data', MotorData, queue_size=10)
    rospy.Subscriber('/ired/motor/speed_fb', MotorSpeed, motorSpeedCallback)
    rospy.Subscriber('/ired/motor/speed_control', MotorControl, motorControlCallback)
    rospy.loginfo("ROS publisher on /ired/speed [geometry_msgs/Twist]")
    rospy.loginfo("ROS publisher on /ired/motor/data [ired_msgs/MotorData]")
    rospy.loginfo("ROS subscriber on /ired/motor/speed_fb [ired_msgs/MotorSpeed]")
    rospy.loginfo("ROS subscriber on /ired/motor/speed_control [ired_msgs/MotorControl]")
    
    while not rospy.is_shutdown():
        motorData()
        motor_data_pub_.publish(motor_data_)
        
        forwardKinematics()
        robot_speed_pub_.publish(robot_speed_)
        
        rate.sleep()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass