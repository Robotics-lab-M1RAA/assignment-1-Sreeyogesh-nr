#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node1():
    rospy.init_node('Sreeyogesh')
    pub = rospy.Publisher('hello_class', String, queue_size=10)
    sub=rospy.Subscriber('welcome', String)
    
    rate = rospy.Rate(1)  # 1 Hz
    
    while not rospy.is_shutdown():
        txt="hello RAA24_26"
        msg=String()
        msg.data=txt
        pub.publish(msg)
        rospy.loginfo(msg.data)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass