#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys
A,B,C,X = list(map(int,[input(),input(),input(),input()]))
A,B,C = list(map(lambda x: x+1, [A,B,C]))
t = 0

for a in range(A):
	if a*500 > X : break
	for b in range(B):
		if a*500 + b*100  > X : break
		for c in range(C):
			SUM = a*500 + b*100 + c*50
			if SUM  > X : break
			elif SUM == X : t += 1

print(t)