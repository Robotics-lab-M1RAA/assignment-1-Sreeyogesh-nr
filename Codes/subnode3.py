#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"received:{msg.data}")


def node3():
    rospy.init_node('CET')
    rospy.Subscriber('hello_college', String, callback)
    rospy.spin()

if __name__== '__main__':
    node3()
