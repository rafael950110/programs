#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys

N,A,B = list(map(int,input().split(" ")))
S = 0

for n in range(N+1) :
	s = sum(list(map(int,str(n))))
	if A <= s <= B :S += n

print(S)