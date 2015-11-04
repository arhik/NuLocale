
import time

import subprocess
import bitstring
import iio
iioContext = iio.Context()
devList = [ dev.name for dev in iioContext.devices ]
print devList
indx = devList.index('accel_3d')%(len(devList)/2)

# from bitstring import BitArray

def read_accel_x():
	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_x_raw".format(indx),"r") as accel_x:
		#x = BitArray(accel_x.read())
		# sint = x.int
		x = int(accel_x.read())
		x = bitstring.Bits(uint=x,length=16)
		[x] = x.unpack('int')
	return (x)

def read_accel_y():
	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_y_raw".format(indx),"r") as accel_y:
		y  = int(accel_y.read())
		y = bitstring.Bits(uint=y,length=16)
		[y] = y.unpack('int')
	return y


def read_accel_z():
	with open("/sys/bus/iio/devices/iio:device{0}/in_accel_z_raw".format(indx),"r") as accel_z:
		z  = int(accel_z.read())
		z = bitstring.Bits(uint=z,length=16)
		[z] = z.unpack('int')
	return z

prev_left = False
prev_right = False
prev_normal = False
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
	time.sleep(2)
	prev_left = left
	prev_right = right
	prev_normal = normal

