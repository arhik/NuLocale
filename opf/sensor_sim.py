#!usr/bin/env python

import sys
import random

import math

import time

class Sensor():
	
	
	def __init__(self):
		import math
		import random
		self.nxt_val_gen = self.sensor_gen()
	
	
	def sensor_gen(self):
		while(1):
			rndm_val = random.random()
			yield rndm_val
	
	def run(self):
		while(1):
			time.sleep(1)
			print(self.nxt_val_gen.next())



if __name__ == '__main__':
	try:
		t = Sensor()
		t.run()
	except KeyboardInterrupt as k:
		sys.exit()

