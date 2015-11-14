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
	ble_pkts_dict = blescan.parse_events(sock, 4)
	print(ble_pkts_dict)
	for mac_id, pkt in  ble_pkts_dict.items():
		print(mac_id,pkt)
		ble_pkt = json.loads(ble_pkts_dict[mac_id])
		if(mac_id == 'd0:39:72:d3:4d:cf'):
			
			d1 = ble_pkt.get("Range",None)
		else:
			d2 = ble_pkt.get("Range",None)

	print(d1,d2)
	# print "----------"
	# print(ble_pkt)
	# print(type(ble_pkt))
	# print(ble_pkt.keys())
	# # print(ble_pkt.get("UUID"))
	# for ble_pkt_mac_address in ble_pkts_dict:
	# 	d1 = ble_pkts_dict if ble_pkt_mac_address=="d0:39:72:d3:4d:cf":


		# UUID = ble_pkt.get("UUID", None)
		# print UUID
		# print(ble_pkt)
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