#!/usr/bin/env python
#coding: utf-8

def main() :
	inData = input().split()
	outData = []
	a = float(inData[0])
	b = float(inData[1])
	R = float(inData[2])
	for i in range(int(input())) :
		inData = input().split()
		x = float(inData[0])
		y = float(inData[1])
		if (x-a) ** 2 + (y-b) ** 2 >= R ** 2 :
			outData.append("silent")
		else :
			outData.append("noisy")

	for i in outData : print(i)

if __name__ == "__main__" :
	main()