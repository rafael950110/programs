#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

N = int(input())
T = [list(map(int,input().split(" "))) for n in range(N)]
t1,x1,y1 = 0,0,0

for [t,x,y] in T :
	m  = abs(x-x1) + abs(y-y1)
	th = t - t1
	# print("[t,x,y] =",[t,x,y],"\t[t1,x1,y1,l] =",[t1,x1,y1,th-m])

	if th >= m and (th - m) % 2 == 0 :
		t1,x1,y1 = t,x,y
	else :
		print("No")
		break
else :
	print("Yes")