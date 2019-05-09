#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import json
import threading
import time
agents = {}

def client_handler(clientsocket, client_address, client_port,):
  global agents

  print '-- LOGIN :',client_address
  msg = json.dumps({'_p':'whoareu'})
  clientsocket.send(msg)
  
  while True:
    try:
      msg = json.loads(clientsocket.recv(1024))
    except OSError : break

    print msg
    if 'sleep' in msg.keys() : time.sleep(msg['sleep'])
    if 'name'  in msg.keys() : 
      agents.update({msg['name']:msg['_p']})

    # if 'name'  in msg.keys() :
    #   agents.update({client_address:{'name':msg['name']}})
    #   sent_msg.update({'_p':'wait'})

    # if '_p' in msg.keys() :
    #   if   msg['_p'] == 'wait': sent_msg.update({'_p':'end'})
    #   elif msg['_p'] == 'end' : break

    # if 'sleep' in msg.keys() : time.sleep(msg['sleep'])

    # while True:
    #   msg = json.dumps(sent_msg)
    #   sent_len = clientsocket.send(msg)
    #   if sent_len == len(msg) : break
    #   msg = msg[sent_len:]
    # print('send to {1} : {0}'.format(msg, client_address))
    print agents
    msg = json.dumps(agents)
    clientsocket.send(msg)


  print "-- LOGOUT :",client_address
  clientsocket.close()


### --- setting server --- ###
def main():

  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

  host = '192.168.116.137'
  port = 50007
  serversocket.bind((host, port))
  serversocket.listen(128)

  while True:
    clientsocket, (client_address, client_port) = serversocket.accept()
    client_thread = threading.Thread( target =  client_handler,
                                      args   =( clientsocket,
                                                client_address,
                                                client_port ))
    client_thread.daemon = True
    client_thread.start()

if __name__ == '__main__':
    main()