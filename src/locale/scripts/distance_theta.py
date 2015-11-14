#!/usr/bin/env python2
import rospy
from std_msgs.msg import Float32MultiArray, Float32
import math
from turtlesim.msg import Pose

t = Float32MultiArray()
def callback(data):
    print(data)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    [x,y,theta] = data.data
    theta = theta if theta>=0 else 2*math.pi - abs(theta)
    y1_ref = 5.55
    x1_ref = 0.00
    y2_ref = 11.1
    x2_ref = 5.55
    y3_ref = 5.55
    x3_ref = 11.1
    y4_ref = 0.00
    x4_ref = 5.55

    # y1_ref = 0.00
    # x1_ref = 0.00
    # y2_ref = 11.1
    # x2_ref = 0.00
    # y3_ref = 11.1
    # x3_ref = 11.1
    # y4_ref = 0.00
    # x4_ref = 11.1

    # x, y = data.x, data.y
    distance1 = math.sqrt((x-x1_ref)**2 + (y- y1_ref)**2)
    distance2 = math.sqrt((x-x2_ref)**2 + (y- y2_ref)**2)
    distance3 = math.sqrt((x-x3_ref)**2 + (y- y3_ref)**2)
    distance4 = math.sqrt((x-x4_ref)**2 + (y- y4_ref)**2)
    # t.data = (distance1,distance2,distance3,distance4, theta)
    t.data = [0,distance2, 0 ,distance4, theta]
    # pub.publish(t)

def callback2(data):
    print(data)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    [x,y] = data.data

    t.data[0] = x
    t.data[2] = y
    pub.publish(t)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("cord_theta", Float32MultiArray, callback)
    rospy.Subscriber("ble_publisher", Float32MultiArray, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('dist_theta', Float32MultiArray, queue_size=10)
    listener()