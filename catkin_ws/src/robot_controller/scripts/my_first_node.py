#!/usr/bin/env python3
import rospy

def node_functionality():

    rospy.loginfo('=== TEST NODE ===')
    
    # 0.5 Hz -> 2 s
    rate = rospy.Rate(hz = 0.5)

    while not rospy.is_shutdown():

        rospy.loginfo('Hello. This will continue until the node is shut down')

    # Error message (maybe it is not an error but I just wanted to use this function)

    rospy.logerr('== NODE HAS BEEN SHUT DOWN')

if __name__ == '__main__':
    # Initialize ROS node (remember to indicate its name)

    rospy.init_node('test_ros_node')

    # Bring up the node functionality

    node_functionality()