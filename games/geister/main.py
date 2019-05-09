#!/usr/bin/env python
#coding: utf-8

class col:
  HEADER		= '\033[95m'
  B 				= '\033[94m'
  G 				= '\033[92m'
  Y 				= '\033[93m'
  R 				= '\033[91m'
  ENDC			= '\033[0m'
  BOLD			= '\033[1m'
  UNDERLINE = '\033[4m'
  RB 		 		= '\033[91m\033[1m'

# p : Player
field = {'player':[[-1 for i in range(6)] for i in range(6)], 'ghost':[["" for i in range(6)] for i in range(6)]}
whenSetGhost = [[[i,j] for i in range(4,6) for j in range(1,5)],[[i,j] for i in range(1,-1,-1) for j in range(4,0,-1)]]

def set_ghosts(player,ghosts):
	if len(ghosts) == 8 :
		for ghost,ij in zip(ghosts,whenSetGhost[player]) :
			[i,j] = ij
			field['player'][i][j] = player
			field['ghost'][i][j]  = ghost
		return field
	else :
		return -1

def move_ghosts(player,ghosts):
	return

def print_field(field) :
	for i,(linePlayer,lineGhost) in enumerate(zip(field['player'],field['ghost'])) :
		for j,(Player,Ghost) in enumerate(zip(linePlayer,lineGhost)) :
			if Player < 0 :
				if i % 5 != 0 or j % 5 != 0 :
					print ".",
				elif j == 0 :
					print "←",
				elif j == 5 :
					print "→",
			elif Player > 0 :
				if Ghost == "g" :
					print col.G + "●" + col.ENDC,
				else :
					print col.Y + "●" + col.ENDC,
			else :
				if Ghost == "g" :
					print col.B + "●" + col.ENDC,
				else :
					print col.R + "●" + col.ENDC,
		print

if __name__ == "__main__" :
	for i in [0,1] :
		print "Player{} : set a ghost >".format(i),
		field = set_ghosts(i,raw_input())
	# field = set_ghosts(0,"gbggbbgb")
	# field = set_ghosts(1,"gbbgbgbg")
	print_field(field)