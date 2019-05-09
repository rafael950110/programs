#!/usr/bin/env python
#coding: utf-8

import json
import numpy as np
from websocket import create_connection

mods = []
for num in range(3*5*7) :
	text = ""
	if not num % 3 : text += "Fizz"
	if not num % 5 : text += "Buzz"
	if not num % 7 : text += "Moi"
	if not text    : text = 0
	mods.append(text)

ws = create_connection("wss://saiyo2019.moi.st/websocket/dc6559af39dd436b9bf12474b78e1069")

ws.send(json.dumps({
   "signal": "start"
}))

while True:
	msg = json.loads(ws.recv())
	# num = msg['number']
	# text = ""

	# if not num % 3 : text += "Fizz"
	# if not num % 5 : text += "Buzz"
	# if not num % 7 : text += "Moi"
	# if not text    : text = num

	num = mods[msg['number'] % 105]
	text = num if num else msg['number']

	ws.send(json.dumps({
		'answer':text
	}))