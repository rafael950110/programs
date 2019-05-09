# -*- coding:utf-8 -*-
 
from threading import Thread, Lock
import time
 
class Ob(object):
	def __init__(self):
		self.v = 0
		self.lock = Lock()
 
	def count(self):
		with self.lock:
			for i in range(self.v):
				print i ,
			print ""
			self.v += 1
 
class Counter(Thread):
	def __init__(self,share_object):
		super(Counter,self).__init__()
		self.share_object = share_object
 
	def run(self):
		while True:
			time.sleep(0.5)
			self.share_object.count()
			if self.share_object.v > 10 : break
 
def main():
	v = Ob()
	t1 = Counter(v)
	t2 = Counter(v)
 
	t1.start()
	t2.start()
 
	t1.join()
	t2.join()
 
if __name__ == '__main__':
	main()