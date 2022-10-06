#!/usr/bin/env python3

from email import message
import rospy
from geometry_msgs.msg import Twist


def draw_circle_func():
    
    coordinates = Twist()

    coordinates.angular.z = 1.0

    coordinates.linear.x = 1.0

    return coordinates


if __name__ == "__main__":

    # Initialize node

    rospy.init_node('draw_cicle')

    # Create a publisher

    publisher = rospy.Publisher(name = "/turtle1/cmd_vel", data_class = Twist, queue_size = 10)

    # Rate = 1 Hz

    rate_time = rospy.Rate(hz = 1)

    while not rospy.is_shutdown():

        message = draw_circle_func()

        publisher.publish(message)

        rospy.loginfo(message)

        rate_time.sleep()