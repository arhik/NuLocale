import pygame, sys
import random
import rospy
import time
from std_msgs.msg import Float64,String, Int64

from geometry_msgs.msg import Vector3
pygame.init()
pygame.mouse.set_visible(False)
windowSize = (800,800)

screen = pygame.display.set_mode(windowSize)

font = pygame.font.SysFont("Times New Roman", 48)

rendered_star = font.render("*", 1, (25, 120, 120), (25,25,25))

rendered_dot  = font.render(".", 1, (25, 12, 120), (25,25,25))
rendered_dot_size = rendered_dot.get_size()


x,y = 0,0

clock = pygame.time.Clock()



pub = rospy.Publisher('sensor_stream', Vector3, queue_size=10)
rospy.init_node('sensor_input_publisher', anonymous=True)
while not rospy.is_shutdown():
	clock.tick(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill((25,25,25))
	mousePosition = pygame.mouse.get_pos()

	x, y = mousePosition

	x1, x2, x3, x4 = x, 800 - x, y, 800, y

	# Quaternion sending...
	# TODO :




	screen.blit(rendered_star, (x,y))
	screen.blit(rendered_dot , (x))
	pygame.display.update()
	rand_x = random.random()
	rand_y = random.random()
	val_x = x + 10*rand_x
	val_y = y + 10*rand_y
	val_z = 0.0
	val = Vector3(val_x, val_y, val_z)
	
	rospy.loginfo("Sent %s at %s" %(val,rospy.get_time()))
	pub.publish(val)

	
