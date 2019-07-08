#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pyxel

class App:
	def __init__(self):
		pyxel.init(100, 120)
		pyxel.run(self.update, self.draw)

	def update(self):
		pass

	def draw(self):
		pyxel.cls(0)
		for i in range(16) :
			x = i * 10
			pyxel.text(x, 10, str(i), 7)
			pyxel.pix(x, 20, i)
			pyxel.line(x, 30, x+8, 40, i)
			pyxel.rect(x, 50, x+8, 60, i)
			pyxel.circ(x+4, 80, 8, i)

App()