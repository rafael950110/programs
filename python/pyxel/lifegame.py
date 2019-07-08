#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pyxel
import sys, random
from copy import deepcopy as cp

class App:
	def __init__(self):

		pyxel.init(160, 160, caption="Life Game", fps=5)

		self.cells  = [[ random.randint(0,1) for i in range(80)] for j in range(80)]
		self.tcells = [[ 0 for i in range(80)] for j in range(80)]
		self.eight  = [ (i,j) for i in [-1,0,1] for j in [-1,0,1] if abs(i) + abs(j)]
		self.run = 1
		self.gen = 1

		pyxel.run(self.update, self.draw)


	def debug_draw(self):
		pyxel.cls(0)
		for i in range(16) :
			x = i * 10
			pyxel.text(x, 10, str(i), 7)
			pyxel.pix(x, 20, i)
			pyxel.line(x, 30, x+8, 40, i)
			pyxel.rect(x, 50, x+8, 60, i)
			pyxel.circ(x+4, 80, 8, i)

	def update(self):
		self.gen += 1
		for y in range(1,79) :
			for x in range(1,79) :
				c = 0
				for e in self.eight :
					if self.cells[ y+e[1] ][ x+e[0] ] : c += 1
				if self.cells[y][x] : 
					if 1 < c < 4 :
						self.tcells[y][x] = 1
					else :
						self.tcells[y][x] = 0
				elif c == 3 :
					self.tcells[y][x] = 1
		self.cells = cp(self.tcells)

	def draw(self):
		for y in range(80) :
			for x in range(80) :
				if self.cells[y][x] :
					pyxel.rect(x*2, y*2, x*2+1, y*2+1, 11)
				else :
					pyxel.rect(x*2, y*2, x*2+1, y*2+1, 0)

if __name__ == '__main__' :
	App()