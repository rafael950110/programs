#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys, random, copy, tkinter, time
import numpy as np
from numpy import sin, cos

SCREEN_WIDTH  = 360
SCREEN_HEIGHT = 360
OVAL = 5
g = 9.8

def calc_ball(x, y, th, l) :
	return x + l*sin(th), y + l*cos(th)

def calc_theta(th, dt, l) :
	om = (G/l) * sin(np.radians(th)) * dt
	return th + om

def calc_v(l, th, high_th) :
	return np.sqrt(2*g*l*(cos(th)-cos(high_th)))

xO, yO = 180, 20
m1 = 1
l1 = 200
th1 = 120.0

x1, y1 = calc_ball(xO, yO, th1, l1)
print(x1,y1)

t  = 0.0
dt = 0.05
v = calc_v(l1, th, 120.0)

root = tkinter.Tk()
root.title(u"random TSP")
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
canvas = tkinter.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT	)
canvas.place(x=0, y=0)
root.title(u"ぶらんこ")


while True :

	canvas.delete('all')	# キャンバスをクリア

	# canvas.create_line(xO, yO, x1, y1, fill='gray', width=2)
	canvas.create_oval(x1 - OVAL, y1 - OVAL, x1 + OVAL, y1 + OVAL, fill='black')

	canvas.update()

root.mainloop()