import rospy
import message_filters
import pygame, sys
from std_msgs.msg import Float32, Float32MultiArray
from geometry_msgs.msg import Vector3

# pygame.init()
# pygame.mouse.set_visible(False)

# windowSize = (800,800)

# screen = pygame.display.set_mode(windowSize)

# font = pygame.font.SysFont("Times New Roman", 48)

# rendered_dot = font.render("*", 1, (25, 120, 120), (250,250,250))

# rendered_dot_size = rendered_dot.get_size()


# x,y = 0,0

# clock = pygame.time.Clock()
vec = [0,0,0]

def callback1(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[0] = data.data
	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		sys.exit()
	# lighton = 1
	# light_color = (60,60,60) if lighton else (130,130,30)
	
	# screen.fill((250,250,250))
	# pygame.draw.rect(screen, light_color, (400,400,100,100),0)

	# screen.blit(rendered_dot, (x,y))
	# pygame.display.update()
def callback2(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[1] = data.data
	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		sys.exit()
	# lighton = 1
	# light_color = (60,60,60) if lighton else (130,130,30)
	
	# screen.fill((250,250,250))
	# pygame.draw.rect(screen, light_color, (400,400,100,100),0)

	# screen.blit(rendered_dot, (x,y))
	# pygame.display.update()
def callback3(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
	print(data)
	vec[2] = float(data.data)
	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		sys.exit()
	# lighton = 1
	# light_color = (60,60,60) if lighton else (130,130,30)
	
	# screen.fill((250,250,250))
	# pygame.draw.rect(screen, light_color, (400,400,100,100),0)
	pub.publish(Vector3(vec[0],vec[1],vec[2]))
	# screen.blit(rendered_dot, (x,y))
	# pygame.display.update()
	
	
def sensory_input_subscriber():
	rospy.init_node("sensory_inference_input_subscriber",anonymous=True)

	rospy.Subscriber("sensory_inference_stream_x", Float32, callback1)
	rospy.Subscriber("sensory_inference_stream_y", Float32,callback2)
	rospy.Subscriber("sensory_inference_stream_z", Float32,callback3)
	
	# inf_x = message_filters.Subscriber("sensory_inference_stream_x",Float64)
	# inf_y = message_filters.Subscriber("sensory_inference_stream_y", Float64)
	# inf_z = message_filters.Subscriber("sensory_inference_stream_z", Float64)

	
	# rospy.Subscriber("sensory_inference_stream_x",Float64, callback)
	rospy.spin()


if __name__=="__main__":
	pub = rospy.Publisher("final_coordinates",Float32MultiArray, queue_size = 10)
	sensory_input_subscriber()

