#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = 'localhost'
port = 50007

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

print "waiting for connections..."
clientsock, client_address = serversock.accept()

while True:
	rcvmsg = clientsock.recv(1024)
	print 'Receved -> %s' % (rcvmsg)
	if rcvmsg == '':
		print "rcvmsg end!!!"
		break
	print 'Type message...'
	s_msg = raw_input()
	if s_msg == '':
		print "s_msg break!!!"
		clientsock.sendall('')
		break
	print 'Wait...'
	clientsock.sendall(s_msg)

clientsock.close()