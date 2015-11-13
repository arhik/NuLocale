import rospy
import message_filters
import pygame, sys
from std_msgs.msg import String,Int64,Float64
from geometry_msgs.msg import Vector3

pygame.init()
pygame.mouse.set_visible(False)

windowSize = (800,800)

screen = pygame.display.set_mode(windowSize)

font = pygame.font.SysFont("Times New Roman", 48)

rendered_dot = font.render("*", 1, (25, 120, 120), (250,250,250))

rendered_dot_size = rendered_dot.get_size()


x,y = 0,0

clock = pygame.time.Clock()


def callback(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec = [0,0,0]
	for i in range(3):
		vec[i] = data
	[x, y, z]   = vec
	print(vec)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	lighton = 1
	light_color = (60,60,60) if lighton else (130,130,30)
	
	screen.fill((250,250,250))
	pygame.draw.rect(screen, light_color, (400,400,100,100),0)

	screen.blit(rendered_dot, (x,y))
	pygame.display.update()
	
def sensory_input_subscriber():
	rospy.init_node("sensory_inference_input_subscriber",anonymous=True)
	inf_x = message_filters.Subscriber("sensory_inference_stream_x",Float64)
	inf_y = message_filters.Subscriber("sensory_inference_stream_y", Float64)
	inf_z = message_filters.Subscriber("sensory_inference_stream_z", Float64)

	ts = message_filters.TimeSynchronizer([inf_x, inf_y, inf_z], 10)

	ts.registerCallback(callback)

	# rospy.Subscriber("sensory_inference_stream_x",Float64, callback)
	rospy.spin()


if __name__=="__main__":
	sensory_input_subscriber()