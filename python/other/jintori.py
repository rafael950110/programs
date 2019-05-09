#!/usr/bin/env python
#coding: utf-8

import re,os,sys,math,pygame
from pygame.locals import *


def main():
	pygame.init()

	LENGTH = 800
	screen = pygame.display.set_mode((LENGTH,LENGTH))
	pygame.display.set_caption("GAME")

	mw,mh = 5,5
	pw,ph = 400,400
	r = 20

	while True:
		screen.fill((180,200,255))
		pygame.draw.ellipse(screen,(240,240,240),(0,0,LENGTH,LENGTH))
		# pygame.draw.polygon(screen, (255,0,0), [[10, 10], [200,200], [10,200]], 0)
		# pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50),5) 

		pw,ph = pw+mw,ph+mh
		if pw < 0 or pw > LENGTH - r : mw *= -1
		if ph < 0 or ph > LENGTH - r : mh *= -1

		font = pygame.font.Font(None, 40)
		text = font.render("pw:"+str(pw), True, (255,255,255))
		screen.blit(text, [20, 20])

		pygame.draw.ellipse(screen,(250,50,50),(pw,ph,r,r))
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

if __name__ == "__main__":
  main()