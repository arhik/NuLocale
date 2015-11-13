
import time
import rospy
import time
from std_msgs.msg import Float64,String, Int64
from geometry_msgs.msg import Vector3
#from sensor import Sensor
import subprocess
import bitstring
#import iio

import os

path = "/sys/bus/iio/devices/"

iio_devices = [dev for dev in os.listdir(path) if dev.startswith('iio')]

iio_dev_names = [ open(path+i+'/name').readline().strip('\n') for i in iio_devices ]
print(iio_devices)

print(iio_dev_names)

accel_indx = iio_dev_names.index('accel_3d') # hard coded ...

magn_indx = iio_dev_names.index('magn_3d')
# iioContext = iio.Context()
# devList = [ dev.name for dev in iioContext.devices ]
# print devList
# indx = devList.index('accel_3d')
# magn_indx = devList.index('magn_3d')
# from bitstring import BitArray



# def read_accel_scale():
# 	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_x_raw".format(accel_indx),"r") as scale_x:
# 		scal_x = 

def read_accel_x():
	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_x_raw".format(accel_indx),"r") as accel_x:
		#x = BitArray(accel_x.read())
		# sint = x.int
		x = int(accel_x.read())
		x = bitstring.Bits(uint=x,length=16)
		[x] = x.unpack('int')
	return (x)

def read_accel_y():
	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_y_raw".format(accel_indx),"r") as accel_y:
		y  = int(accel_y.read())
		y = bitstring.Bits(uint=y,length=16)
		[y] = y.unpack('int')
	return y


def read_accel_z():
	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_z_raw".format(accel_indx),"r") as accel_z:
		z  = int(accel_z.read())
		z = bitstring.Bits(uint=z,length=16)
		[z] = z.unpack('int')
	return z

def magn_read():
	with open("/sys/bus/iio/devices/iio:device{0}/in_rot_from_north_magnetic_tilt_comp_raw".format(magn_indx),"r") as magn_north:
		n = int(magn_north.read())
		#n = bitstring.Bits(uint=n,length=16)
		#[n] = n.unpack('int')
	return n


prev_left = False
prev_right = False
prev_normal = False

def run():
	while True:
		left = read_accel_x()>400
		right = read_accel_x()<-400
		normal = ~(left^right)
		print "%s : %s : %s" %(read_accel_x(),read_accel_y(),read_accel_z())
		if(left):
			if (left^prev_left):
				subprocess.call(['xbacklight','-set','5'])
				subprocess.call(['xrandr','--output', 'eDP1', '--rotate', 'left'])
				subprocess.call(['xinput', 'set-prop', 'NTRG0001:01 1B96:1B05 Pen', 'Coordinate Transformation Matrix', '0', '-1', '1', '1', '0', '0', '0', '0', '1'])
				subprocess.call(['xbacklight','-set','50'])
		
		elif right:
			if(prev_right ^ right):
				subprocess.call(['xbacklight','-set','5'])
				subprocess.call(['xrandr','--output', 'eDP1', '--rotate', 'right'])
				subprocess.call(['xinput', 'set-prop', 'NTRG0001:01 1B96:1B05 Pen', 'Coordinate Transformation Matrix', '0', '1', '0', '-1', '0', '1', '0', '0', '1'])
				subprocess.call(['xbacklight','-set','50'])
		elif normal:
			if( prev_normal ^ normal):
				subprocess.call(['xbacklight','-set','5'])
				subprocess.call(['xrandr','--output','eDP1','--rotate','normal'])
				subprocess.call(['xinput', 'set-prop', 'NTRG0001:01 1B96:1B05 Pen', 'Coordinate Transformation Matrix', '1', '0', '0', '0', '1', '0', '0', '0', '1'])
				subprocess.call(['xbacklight','-set','50'])
		time.sleep(.5)
		prev_left = left
		prev_right = right
		prev_normal = normal


def sensor_input_publisher():
	pub = rospy.Publisher('sensor_stream', Vector3, queue_size=10)
	rospy.init_node('sensor_input_publisher', anonymous=True)
	while not rospy.is_shutdown():
		val_x= float(read_accel_x())
		val_y= float(read_accel_y())
		val_z= float(read_accel_z())
		val = Vector3(val_x, val_y, val_z)
		rospy.loginfo("Sent %s at %s" %(val,rospy.get_time()))
		pub.publish(val)
		#time.sleep(0.1)

if __name__=='__main__':
	try:
		#run()
		sensor_input_publisher()
	except rospy.ROSInterruptException:
		pass
