#!/usr/bin/env python
# -*- coding:utf-8 -*-

def Fizz_Buzz_Moi(target = 105) :
	mods = []
	# target = 246194674
	for num in range(3*5*7) :
		text = ""
		if not num % 3 : text += "Fizz"
		if not num % 5 : text += "Buzz"
		if not num % 7 : text += "Moi"
		if not text    : text = 0
		mods.append(text)

	num = mods[target % 105]
	text = num if num else target
	print text


if __name__ == '__main__' :
	print "input num :",
	Fizz_Buzz_Moi(int(raw_input()))