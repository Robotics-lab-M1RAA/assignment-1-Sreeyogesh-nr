#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def subs(msg):
    rospy.loginfo(f"{msg.data}")

rospy.init_node("RAA24_subnode")
rospy.Subscriber("Greetings",String,subs)
rospy.spin()

