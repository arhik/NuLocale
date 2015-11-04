#!user/python/env python2
import pyautogui as auto
import sys
auto.FAILSAFE = True
def auto_mouse():
	auto.moveTo(450,450)
	pos = auto.position()

	auto.moveRel(-200,-200)
	pos2  = auto.position()
	for i in range(100 ):
		try:
			auto.moveTo(pos, duration = 1, tween = auto.easeInCubic)
			auto.click()
			auto.moveTo(pos, duration = 1)
			auto.click()
			auto.moveTo(pos2,duration = 1, tween = auto.easeInQuad)
		except:
			sys.exit()

if __name__=="__main__":
	try:
		auto_mouse()

	except:
		sys.exit()
