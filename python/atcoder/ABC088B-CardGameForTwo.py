#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys

a = list(input())
a = sorted(list(map(int,input().split(" "))), key= lambda x: -x)
test = lambda a, L1=0, L2=0, f=lambda f, L1, L2, a : f(f,L2,L1+a.pop(0),a) if len(a) else print(abs(L1-L2)) : f(f, L1, L2, a)
test(a)