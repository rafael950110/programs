#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800,800))

cells  = [[ 0 for i in range(40)] for j in range(40)]
tcells = [[ 0 for i in range(40)] for j in range(40)]
eight  = [ (i,j) for i in [-1,0,1] for j in [-1,0,1] if abs(i) + abs(j)]

while True :
	screen.fill((255,255,255))
	for y in range(40) :
		for x in range(40) :
			if cells[y][x] == 1:
				rect = Rect(x*20, y*20, 20, 20)
				pygame.draw.rect(screen,(0,255,0),rect)

	for e in pygame.event.get() :
		if e.type == MOUSEBUTTONDOWN :
			mx, my = int(e.pos[0]/20), int(e.pos[1]/20)
			cells[my][mx] = 1 - cells[my][mx]
		if e.type == QUIT :
			pygame.quit()
			sys.exit()

	pygame.display.update()