#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
 
 
HOST = 'localhost'
PORT = 50007
clients = []
 
def input_msg_roop(sock):
  """メッセージ入力を促し、サーバに送信する"""
  while True :
    msg = raw_input('>>>')
    if msg == 'exit':
      break
    elif msg:
      sock.send(msg.encode('utf-8'))

 
def remove_conection(con, address):
  """クライアントと接続を切る"""

  print('[切断]{}'.format(address))
  con.close()
  clients.remove((con, address))
 
 
def server_start():
  """サーバをスタートする"""

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

    try:
        input_msg_roop(con)
    finally:
        sock.close()

 
def handler(con, address):
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
        print("[受信]{} - {}".format(address, data.decode("utf-8")))
        for c in clients:
          c[0].sendto(data, c[1])
 
 
if __name__ == "__main__":
    server_start()