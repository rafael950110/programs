#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

L = [input()]
L = list(map(int,input().split(" ")))

test = lambda L, N=0, F=lambda F,L,N : F(F,[int(l/2) for l in L],N+1) if all([l%2==0 for l in L]) else print(N) : F(F,L,N)
test(L)