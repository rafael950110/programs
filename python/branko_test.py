#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys, random, copy, tkinter, time
import numpy as np
from numpy import sin, cos

SCREEN_WIDTH  = 360
SCREEN_HEIGHT = 360
OVAL = 5
G = 9.8

def calc_ball(x, y, th, l) :
	return x + l*sin(th), y + l*cos(th)

def calc_theta(th, dt, l) :
	om = -(G/l) * sin(np.radians(th)) * dt
	return th + om

xO, yO = 180, 20
m1 = 1
l1 = 200
th1 = 30.0

for i in range(720) :

	th1 = calc_theta(th1, 0.05, l1)
	x1, y1 = calc_ball(xO, yO, th1, l1)

	print(xO, yO, x1, y1)
	print(x1 - OVAL, y1 - OVAL, x1 + OVAL, y1 + OVAL)
