#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys, random, copy, tkinter, time
import numpy as np
from numpy import sin, cos

SCREEN_WIDTH  = 360
SCREEN_HEIGHT = 360
OVAL = 5
g = 9.8

the = np.pi/3
l_len = 100
ox, oy = 180, 100
fx, fy = sin(the)*l_len + ox, cos(the)*l_len + oy
dt = 0.1
dx, dy = 0, 0
vec = 0

root = tkinter.Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
canvas = tkinter.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT	)
canvas.place(x=0, y=0)
root.title(u"ぶらんこ")


while True :

	canvas.delete('all')	# キャンバスをクリア

	# --- cos,sin calc
	cos_t = (fy - oy) / np.sqrt( (fx-ox)**2 + (fy-oy)**2 )
	sin_t = (fx - ox) / np.sqrt( (fx-ox)**2 + (fy-oy)**2 )

	# --- dx,dy calc
	# omg = -g / l_len * sin_t
	# alp = omg * l_len
	# vec += alp * dt
	vec += -g * sin_t * dt
	dx  = vec * cos_t * dt
	dy  = -vec * sin_t * dt

	# --- update fx,fy
	fx += dx
	fy += dy

	canvas.create_oval(ox - OVAL, oy - OVAL, ox + OVAL, oy + OVAL)
	canvas.create_oval(fx - OVAL, fy - OVAL, fx + OVAL, fy + OVAL, fill='black')
	canvas.create_line(ox, oy, fx, fy,  fill="black", width=2)

	canvas.update()

root.mainloop()