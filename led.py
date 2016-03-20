from rgbmatrix import RGBMatrix
import random, threading
from time import sleep



def dowork():
	print "hello"
	#while True:
	  #wlen = random.random()
	  #sleep(wlen) # Emulate doing some work
	  #print 'work done in %0.2f seconds' % wlen
  
def run():
	print "Running LED service"
	_thread = threading.Thread(target=dowork)
	_thread.setDaemon(True)
	_thread.start()
	
	
def test():
	print "test"