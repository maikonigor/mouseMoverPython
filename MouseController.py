import pyautogui as gui
import sys

from Xlib import X, display

d = display.Display()
s = d.screen()
root = s.root

class MouseController:

	width = 0
	height = 0

	def __init__(self):
		width, heigth = gui.size()
		gui.FAILSAFE = False

	def setPosition(self, x, y):
		self.moveX(x,y)

	def moveX(self, x, y):
		root.warp_pointer(x,y)
		d.sync()
		
	def movePgui(x, y):
		gui.moveTo(x,y, duration=0)
		sys.stdout.flush()

	def getCurrentPosition(self):
		return gui.position()

	def moveFromHere(self, x, y):
		gui.moveRel(x, y)

	def click(self):
		gui.click()

	def rightClick(self):
		gui.click(button='right')