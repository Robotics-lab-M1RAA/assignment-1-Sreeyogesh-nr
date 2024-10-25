#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def publisher_node():
    rospy.init_node('Sreeyogesh_node1', anonymous=True)
    pub = rospy.Publisher('Greetings', String, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hello, I am Sreeyogesh"
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass