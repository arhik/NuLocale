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

rendered_dot = font.render("*", 1, (25, 120, 120), (25,25,25))

rendered_dot_size = rendered_dot.get_size()


x,y = 0,0

clock = pygame.time.Clock()




#auto_mouse()
if(__name__=="__main__"):
	pub = rospy.Publisher('sensor_stream', Vector3, queue_size=10)
	rospy.init_node('sensor_input_publisher', anonymous=True)
	light_toggle = 0
	light_color = (30,30,30)
	mouse_mode = None
	while not rospy.is_shutdown():
		
		try:
			if mouse_mode==None:
			
				mouse_mode = "I am running already"
			clock.tick(10)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.K_DOWN:
					sys.exit()

				elif event.type ==pygame.MOUSEBUTTONDOWN:
					light_toggle = 1 if light_toggle==0 else 0
					light_color = (240,220,250) if light_toggle else (130,130,130)
			screen.fill((25,25,25))
			mousePosition = pygame.mouse.get_pos()
			x, y = mousePosition
			screen.blit(rendered_dot, (x,y))
			pygame.draw.rect(screen, light_color, (400,400,100,100),0)
			pygame.display.update()
			rand_x = random.random()
			rand_y = random.random()
			val_x = x + 100*rand_x
			val_y = y + 100*rand_y
			val_z = float(light_toggle)
			val = Vector3(val_x, val_y, val_z)
			
			rospy.loginfo("Sent %s at %s" %(val,rospy.get_time()))
			pub.publish(val)

		except KeyboardInterrupt:
			sys.exit()


	
