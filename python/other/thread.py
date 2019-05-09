#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time
import datetime

class TestThread(threading.Thread):

  def __init__(self, n, t):
    super(TestThread, self).__init__()
    self.n = n
    self.t = t

  def run(self):
    print " === start sub thread (sub class) === "
    for i in range(self.n):
      time.sleep(self.t)
      print "sub thread (sub class) : " + str(datetime.datetime.today())
    print " === end sub thread (sub class) === "

if __name__ == '__main__':
  th_cl = TestThread(5, 5)
  th_cl.start()
