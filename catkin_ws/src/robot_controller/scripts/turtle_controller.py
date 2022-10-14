#!/usr/bin/env python3

import rospy
# In order to publish in the topic /turtle1/cmd_vel, we need the class Twist
from geometry_msgs.msg import Twist
# In order to subscribe to the topic /turtle1/pose, we need the class Pose
from turtlesim.msg import Pose

def callback_turtle_controller(message : Pose):

    turtle_movement = Twist()
    
    # Getting the turtle's x position
    
    x_coord = message.x

    # Getting the turtle's y position

    y_coord = message.y

    # Check if the turtle is within limits

    is_not_within_limits = x_coord < 2.0 or x_coord > 9.0 or y_coord < 2.0 or y_coord > 9.0

    if is_not_within_limits:

        turtle_movement.linear.x = 1.0

        turtle_movement.angular.z = 1.4

    else:

        turtle_movement.linear.x = 5.0

        turtle_movement.angular.z = 0.0

    publisher.publish(turtle_movement)


if __name__ == '__main__':
    
    # Initializing the ros node

    rospy.init_node('turtle_controller')

    # Creating a publisher (this node will be publishing in the topic /turtle1/cmd_vel)

    publisher = rospy.Publisher(name = '/turtle1/cmd_vel', data_class = Twist, queue_size = 10)

    # Creating a subscriber (this node will be subscribing to the topic /turtle1/pose)

    subscriber = rospy.Subscriber(name = '/turtle1/pose', data_class = Pose, callback = callback_turtle_controller)

    # Keep listening to arriving data until the node is shut down

    rospy.spin()
