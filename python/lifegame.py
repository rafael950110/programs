#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys, random


cells  = [[ random.randint(0,1) for i in range(40)] for j in range(40)]
tcells = [[ 0 for i in range(40)] for j in range(40)]
eight  = [ (i,j) for i in [-1,0,1] for j in [-1,0,1] if abs(i) + abs(j)]

def rule(cells, eight, tcells) :
	for y in range(1,39) :
		for x in range(1,39) :
			c = 0
			for e in eight :
				if cells[ y+e[1] ][ x+e[0] ] : c += 1
			if cells[y][x] : 
				if 1 < c < 4 :
					tcells[y][x] = 1
				else :
					tcells[y][x] = 0
			elif c == 3 :
				tcells[y][x] = 1

	return tcells

pygame.init()
screen = pygame.display.set_mode((800,800))
font = pygame.font.Font(None, 28)
run = 0
gen = 1

while True :
	screen.fill((255,255,255))

	if run :
		gen += 1
		cells = rule(cells, eight, tcells)
		pygame.time.wait(250)

	for y in range(40) :
		for x in range(40) :
			if cells[y][x] :
				rect = Rect(x*20, y*20, 20, 20)
				pygame.draw.rect(screen, (0,255,255), rect)

	for e in pygame.event.get() :

		if e.type == MOUSEBUTTONDOWN and e.button == 1 and not run :

			mx, my = int(e.pos[0]/20), int(e.pos[1]/20)
			print(mx,my,cells[my][mx])
			if mx == 0 or mx == 39 or my == 0 or my == 39 :
				cells[my][mx] = 0
			else :
				cells[my][mx] = 1 - cells[my][mx]

		if e.type == MOUSEBUTTONDOWN and e.button == 2 and not run :
			run = 1 - run

		if e.type == MOUSEBUTTONDOWN and e.button == 3 and not run :
			cells  = [[ 0 for i in range(40)] for j in range(40)]
			gen = 1

		if e.type == QUIT :
			pygame.quit()
			sys.exit()

	s1 = "running" if run == 1 else "setting"
	s2 = "genetarion : " + str(gen)
	text = font.render(s1 + "   " + s2, True, (0,0,0))
	screen.blit(text,(1,1))
	pygame.display.update()