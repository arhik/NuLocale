#!/usr/bin/env python2
import rospy
import message_filters
import pygame, sys
from std_msgs.msg import String,Int64,Float32MultiArray, Float32	
from geometry_msgs.msg import Vector3

vec = [0,0,0,0,0]
t = Float32MultiArray()
def callback1(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[0] = data.data

def callback2(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[1] = data.data

def callback3(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[2] = float(data.data)
	

def callback4(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[3] = float(data.data)
	

def callback5(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[4] = float(data.data)
	t.data = vec
	pub.publish(t)

	
def sensory_input_subscriber():
	rospy.init_node("sensory_inference_input_subscriber",anonymous=True)

	rospy.Subscriber("sensory_inference_stream_d1", Float32, callback1)
	rospy.Subscriber("sensory_inference_stream_d2", Float32,callback2)
	rospy.Subscriber("sensory_inference_stream_d3", Float32,callback3)
	rospy.Subscriber("sensory_inference_stream_d4", Float32,callback4)
	rospy.Subscriber("sensory_theta", Float32,callback5)


	
	# rospy.Subscriber("sensory_inference_stream_x",Float64, callback)
	rospy.spin()


if __name__=="__main__":
	pub = rospy.Publisher("final_coordinates",Float32MultiArray, queue_size = 10)
	sensory_input_subscriber()

