#!/usr/bin/python
# -*- Coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def createParce(w1, w2, b) :
	def func(x1, x2):
		x 	= np.array([x1, x2])
		w		= np.array([w1, w2])
		tmp = np.sum(w*x) + b
		if tmp <= 0 : return 0
		else				: return 1
	return func

def conbineParce(func_main, func1, func2) :
	def func(x1, x2) :
		return func_main(func1(x1,x2),func2(x1,x2))
	return func

def sigmoid(x) :
	return 1 / (1+np.exp(-x))

def relu(x) :
	return np.maximum(0, x)

def identity_function(x) :
	return x

def softmax(x) :
	maximum = np.max(x)
	return np.exp(x-maximum) / np.sum(exp_x)

if __name__ == '__main__' :

	p = {} # パース配列
	p.update({'AND' :createParce(0.5, 0.5, -0.7)})
	p.update({'OR'  :createParce(0.5, 0.5, -0.2)})
	p.update({'NAND':createParce(-0.5, -0.5, 0.7)})
	p.update({'XOR' :conbineParce(p['AND'], p['OR'], p['NAND'])})
	p.update({'XOR2':lambda x1, x2 :p['AND'](p['OR'](x1,x2), p['NAND'](x1,x2))})

	for k,v in p.items() :
		print("{:<5}: ".format(k), end="")
		for i,j in [(i,j) for i in range(2) for j in range(2)] :
			print(v(i,j), end=" ")
		print()