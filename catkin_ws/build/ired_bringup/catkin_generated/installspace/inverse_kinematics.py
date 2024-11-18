#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from ired_msgs.msg import MotorControl
import math
import numpy as np

cmd_vel_ = Twist()
motor_control_ = MotorControl()

def PIDSetup():
    global motor_control_
    motor_control_.pid_motor_front_left[0] = 5
    motor_control_.pid_motor_front_left[1] = 2.5
    motor_control_.pid_motor_front_left[2] = 0.00
    motor_control_.pid_motor_front_right[0] = 5
    motor_control_.pid_motor_front_right[1] = 2.5
    motor_control_.pid_motor_front_right[2] = 0.00
    motor_control_.pid_motor_rear_left[0] = 5
    motor_control_.pid_motor_rear_left[1] = 2.5
    motor_control_.pid_motor_rear_left[2] = 0.00
    motor_control_.pid_motor_rear_right[0] = 5
    motor_control_.pid_motor_rear_right[1] = 2.5
    motor_control_.pid_motor_rear_right[2] = 0.00
    
def inverse_kin_cal(vx, vy, w, deg):
    deg = np.radians(deg)
    wheel_radius = 0.06  # in meters (adjust to your wheel's radius)
    robot_radius = 0.22  # distance from center of robot to each wheel, adjust as needed
    return -(60 / (2 * math.pi * wheel_radius)) * (-1 * vx*np.sin(deg) + vy*np.cos(deg) + -1 * w * robot_radius)
    

def inverseKinematics():
    global motor_control_, cmd_vel_
    Vx = cmd_vel_.linear.x
    Vy = cmd_vel_.linear.y
    W = cmd_vel_.angular.z
    # motor_control_.speed = [-(60 / (2 * math.pi * wheel_radius)) * ((-1 * Vx) + (-1 * Vy) + (-robot_radius * W)),  # Swap BR to FL
    #                         (60 / (2 * math.pi * wheel_radius)) * ((1 * Vx) + (1 * Vy) + (-robot_radius * W)),    # Keep FR as is
    #                         (60 / (2 * math.pi * wheel_radius)) * ((-1 * Vx) + (1 * Vy) + (robot_radius * W)),  # Keep BL as is
    #                         -(60 / (2 * math.pi * wheel_radius)) * ((1 * Vx) + (-1 * Vy) + (robot_radius * W))] # Swap FL to BR
    
    # [FL FR BL BR]
    motor_control_.speed = [inverse_kin_cal(Vx, Vy, W, 135),
                            inverse_kin_cal(Vx, Vy, W, 45),
                            inverse_kin_cal(Vx, Vy, W, 225),
                            inverse_kin_cal(Vx, Vy, W, 315)]




def commandVelocityCallback(msg):
    global cmd_vel_
    cmd_vel_ = msg

def main():
    global motor_control_
    rospy.init_node('inverse_kinematics_node')
    rate = rospy.Rate(10)
    motor_control_pub_ = rospy.Publisher('/ired/motor/speed_control', MotorControl, queue_size=10)
    rospy.Subscriber('/cmd_vel', Twist, commandVelocityCallback)
    rospy.loginfo("ROS publisher on /ired/motor/speed_control [ired_msgs/MotorControl]")
    rospy.loginfo("ROS subscriber on /cmd_vel [geometry_msgs/Twist]")
    PIDSetup()
    
    while not rospy.is_shutdown():
        inverseKinematics()
        motor_control_pub_.publish(motor_control_)
        
        rate.sleep()
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass