#!/usr/bin/env python
#coding: utf-8

def numas(char) :
	return 47 < ord(char) < 58

def priority(A,B) :
	operator = {"+":1,"-":1,"*":2,"/":2}
	if 39 < ord(A) < 42 or 39 < ord(B) < 42 :
		return False
	else :
		return operator[A] >= operator[B]

def main() :
	line = list(input())
	num = 0
	po = []
	op = []

	for char in line :
		if numas(char) :
			num = num * 10 + int(char)
			continue
		if num :
			po.append(num)
			op.append(char)
			num = 0

		if len(op) > 1 and priority(op[-2],op[-1]) :
			po.append(op[-2])
			del op[-2]

		if op[-1] == ")" :
			for i in reversed(op[:-1]) :
				if i == "(" : break
				po.append(i)
				def op


	if num : po.append(num)
	for i in reversed(op) : po.append(i)
	return po

if __name__ == "__main__" :
	po = main()
	for i in po : print(i, end="")
	print("\n")
