#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def pose_callback(message : Pose):
    
    # Retreiving x coordinate

    x_coord = message.x

    # Retreiving y coordinate

    y_coord = message.y

    # Printing (x,y) coordinates of the turtle

    rospy.loginfo(f'Current coordinates: ({x_coord}, {y_coord})')
    

if __name__ == '__main__':

    # Initializing the ros node

    rospy.init_node('turtle_pose_node')

    # Creating the subscriber

    pose_subscriber = rospy.Subscriber(name = '/turtle1/pose', data_class = Pose, callback = pose_callback)

    # Keep listening to arriving data until the node is shut down

    rospy.spin()