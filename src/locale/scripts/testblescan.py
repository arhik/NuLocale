#!/usr/bin/env python 
# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import math
import json
import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

# while True:
try:
	ble_pkt_set = blescan.parse_events(sock, 4)
	# print "----------"
	# print(ble_pkt)
	# print(type(ble_pkt))
	# print(ble_pkt.keys())
	# # print(ble_pkt.get("UUID"))
	for ble_json_pkt in ble_pkt_set:
		ble_pkt = json.loads(ble_json_pkt)
		UUID = ble_pkt.get("UUID", None)
		# print UUID
		if UUID is not None:
			if UUID == "a495ff10c5b14b44b5121370f02d74de":
				
				"""
				# 	RSSI = TxPower - 10 * n * lg(d)
				# 	n = 2 (in free space)
				# 	d = 10 ^ ((TxPower - RSSI) / (10 * n))
				# 	"""
				ratio = float(ble_pkt["RSSI"])/float(ble_pkt["TX_POW"])
				d1 = 0.89976*(ratio**7.7095 + 0.111)
				print("I found bean : {0}".format(d1))
			elif UUID == "234454cf6d4a0fadf2f4911ba9ffa600":
				ratio = float(ble_pkt["RSSI"])/float(-59)
				d2 = 0.89976*(ratio**7.7095 + 0.111)
				print("I found phone : {0}".format(d2))

			else:
				print(ble_pkt)
	# 	print "Estimated distance of beacon : {0}".format(d)
	# if(ble_pkt["UUID"]=="a495ff10c5b14b44b5121370f02d74de"):
	# 	print("tested")
	# if(ble_pkt['MAC_ADDRESS'] =='d0:39:72:d3:4d:cf'):
	# 	"""
	# 	RSSI = TxPower - 10 * n * lg(d)
	# 	n = 2 (in free space)
	# 	d = 10 ^ ((TxPower - RSSI) / (10 * n))
	# 	"""
	# 	d = 10**((ble_pkt["TX_POW"] - ble_pkt["RSSI"])/10*2)
	# 	print "Estimated distance of beacon : {0}".format(d)


except KeyboardInterrupt:
	sys.exit(1)