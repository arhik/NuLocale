#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32MultiArray

t = Float32MultiArray()
t.data = [1,2,4,6,2]
def talker():
    pub = rospy.Publisher('chatter', Float32MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        rospy.loginfo(t)
        pub.publish(t)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass