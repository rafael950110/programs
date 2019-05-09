#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys

S = input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")

if S:
    print("NO")
else:
    print("YES")

# この先、ボツ
# S = input()
# T = ['dream','erase','dreamer','eraser']

# while S :
# 	for t in T :
# 		if t == S[-1*len(t):] :
# 			S = S[:-1*len(t)]
# 			continue

# 	print("NO")
# 	sys.exit()

# print("YES")