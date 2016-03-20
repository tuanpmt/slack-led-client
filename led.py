from rgbmatrix import RGBMatrix
import random, threading
from time import sleep

import json
import led_settings

class LedService:
	def __init__(self):
		print "Loading LED configurations"
		
		with open('led.json', 'r') as f:
			self.data = json.load(f)
			f.close()
		
		self.rows = self.data["settings"]["rows"]
		self.chain = self.data["settings"]["chain"]
		self.parallel = self.data["settings"]["parallel"]
		print (self.rows, self.chain, self.parallel)
		
		self.matrix = RGBMatrix(self.rows, self.chain, self.parallel)
		
	def dowork(self):
		print "Loading scene"
	

	def run(self):
		print "Starting LED service"
	
		self._thread = threading.Thread(target=self.dowork)
		self._thread.setDaemon(True)
		self._thread.start()
		
		
	def stop(self):
		self.matrix.clear()