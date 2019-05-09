#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import json
import time
 
HOST = 'localhost'
PORT = 50007
clients = []
agents = {}
 
def remove_conection(con, address):
  print "-- REMOVE CONECTION",address
  con.close()
  clients.remove((con, address))
 
def server_start():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((HOST, PORT))
  sock.listen(10)

  while True:
    con, address = sock.accept()
    clients.append((con, address))
    handle_thread = threading.Thread(target=handler,
                                     args=(con, address))
    handle_thread.daemon = True
    handle_thread.start()

 
def handler(con, address):
  global agents

  while True:
    try:
      data = con.recv(1024)
    except ConnectionResetError:
      remove_conection(con, address)
      break
    else:
      if not data:
        remove_conection(con, address)
        break
      else:
        msg = json.loads(data)
        if 'sleep' in msg.keys() : time.sleep(msg['sleep'])
        if 'name'  in msg.keys() : agents.update({msg['name']:msg['_p']})

        for c in clients:
          c[0].sendto(data, c[1])
 
 
if __name__ == "__main__":
    server_start()