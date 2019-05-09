#!/usr/bin/env python
#coding: utf-8

import socket
import json
from contextlib import closing

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

card_num = 3
players = 4

class CardInfo :
	num = 0
	col = ""
	open = False

def send_msg(send_msg):
	soc.send(json.dumps(send_msg))
	recv_msg = json.loads(soc.recv(4096))
	print "send>",send_msg
	print "recv>",recv_msg
	return recv_msg

def INITIALIZE() :
	global card_num
	for i in range(card_num) :
		DRAW()

def DRAW() :
	msg = {'_p':"request" , 'func':"draw",'type':"card",'from':"stock",'when':"owner",'num':"1"}		
	send_msg(msg)

def ATTACK() :
	msg = {'_p':"request" , 'func':"attack"}
	msg.update({'type':"card"})
	msg.update({'cost':"owner"})
	target = ""
	msg.update({'success':["open","target"]})
	msg.update({'fail':["open","owner"]})
	while 1 :
		msg.update({'target':"where"})
		recv_msg = send_msg(msg)
		if 'false' == recv_msg['result'] : break

def main() :
	INITIALIZE()
	i = 0
	msg = {'_p':'game','num':i}
	while msg['_p'] != 'end' :
		msg = {'_p':'game','num':i}
		msg = send_msg(msg)
		DRAW()
		ATTACK()
		i += 1

if __name__ == "__main__" :
	global soc
	soc.connect(("localhost", 50007))
	main()
	send_msg({'_p':"break"})
	soc.close()