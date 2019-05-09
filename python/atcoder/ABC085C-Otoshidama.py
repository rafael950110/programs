#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys

X,Y = list(map(int,input().split(" ")))

for i in range(X+1) :
	if i*10000 > Y : break
	for j in range(X-i+1) :
		k = X-i-j
		S = i*10000 + j*5000 + k*1000
		if S > Y : break
		elif S == Y :
			print(i,j,k)
			sys.exit()
print("-1 -1 -1")