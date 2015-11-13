#!/usr/bin/env python

import blescan
import sys
import math
import json
import bluetooth._bluetooth as bluez



import rospy
from std_msgs.msg import String, Float32MultiArray

t = Float32MultiArray()
    
    

if __name__ == '__main__':

	dev_id = 0
	try:
		sock = bluez.hci_open_dev(dev_id)
		print "ble thread started"
	except:
		print "error accessing bluetooth device..."
	    	sys.exit(1)

	blescan.hci_le_set_scan_parameters(sock)
	blescan.hci_enable_le_scan(sock)
	try:
		rospy.init_node('ble_publisher', anonymous=True)
		pub = rospy.Publisher('ble_publisher', Float32MultiArray, queue_size=10)
		
		rate = rospy.Rate(10) # 10hz
		while not rospy.is_shutdown():
			ble_pkt_set = blescan.parse_events(sock, 4)
			distances = []
			for ble_json_pkt in ble_pkt_set:
				ble_pkt = json.loads(ble_json_pkt)
				UUID = ble_pkt.get("UUID", None)
				distances.append(ble_pkt.get("Range",None))
				# print UUID
				# if UUID is not None:
				# 	if UUID == "a495ff10c5b14b44b5121370f02d74de":
				# 		"""
				# 		RSSI = TxPower - 10 * n * lg(d)
				# 		# 	n = 2 (in free space)
				# 		# 	d = 10 ^ ((TxPower - RSSI) / (10 * n))
				# 		# 	"""
				# 		ratio = float(ble_pkt["RSSI"])/float(ble_pkt["TX_POW"])
				# 		d1 = 0.89976*(ratio**7.7095 + 0.111)
				# 		print("I found bean : {0}".format(d1))
				# 	elif UUID == "2f234454cf6d4a0fadf2f4911ba9ffa6":
				# 		ratio = float(ble_pkt["RSSI"])/float(-59)
				# 		d2 = 0.89976*(ratio**7.7095 + 0.111)
				# 		print("I found phone : {0}".format(d2))
				# 	else:
				# 		print(ble_pkt)
			t.data = distances
			rospy.loginfo(t)
			pub.publish(t)
			rate.sleep()
	except rospy.ROSInterruptException:
		pass
