#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

L = [input()]
L = sorted(list(map(int,input().split())), key= lambda x: -x)
test = lambda L, S=0, f=lambda f, L, S : f(f,L[2:],S+L[1]) if L else print(S): f(f, L, S)
test(L)