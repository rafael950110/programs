#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys

a = []
N = int(input())

for i in range(N) :
	n = int(input())
	if n not in a :
		a.append(n)

print(len(a))