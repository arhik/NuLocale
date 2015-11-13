
import rospy

from std_msgs.msg import String,Int64,Float64
from geometry_msgs.msg import Vector3
def callback(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
def sensory_input_subscriber():
	rospy.init_node("sensory_input_subscriber",anonymous=True)
	rospy.Subscriber("sensor_stream",Vector3, callback)
	rospy.spin()

if __name__=="__main__":
	sensory_input_subscriber()
