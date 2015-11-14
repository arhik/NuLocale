#!/usr/bin/env python
import rospy
import pygame, sys
from std_msgs.msg import String,Int64,Float32MultiArray

pygame.init()
pygame.mouse.set_visible(False)

windowSize = (800,800)

screen = pygame.display.set_mode(windowSize)


x,y = 0,0

clock = pygame.time.Clock()

lighton = 1
def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
    d1, d2, d3, d4, theta = data.data
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    light_color = (60,160,160) if lighton else (30,30,30)
    
    screen.fill((250,250,250))
    pygame.draw.circle(screen, light_color, (int(d1*80), 400), 8)
    pygame.draw.circle(screen, lighton, (800-int(d3*80), 400), 8)
    pygame.display.update()
    
def sensory_input_subscriber():
    rospy.init_node("sensory_final_subscriber",anonymous=True)
    rospy.Subscriber("final_coordinates",Float32MultiArray, callback)
    rospy.spin()

if __name__=="__main__":
    sensory_input_subscriber()