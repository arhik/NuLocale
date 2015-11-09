#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32MultiArray

from turtlesim.msg import Pose

t = Float32MultiArray()
def callback(data):
    print(data)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    x1, x2, theta = data.x, data.y, data.theta
    t.data = (x1,x2,theta)
    pub.publish(t)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("turtle1/pose", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('cord_theta', Float32MultiArray, queue_size=10)
    listener()