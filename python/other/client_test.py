#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
 
 
HOST = 'localhost'
PORT = 50007
 
 
def input_msg_roop(sock):
    """メッセージ入力を促し、サーバに送信する"""
 
    while True:
        msg = raw_input('>>>')
        if msg == 'exit':
            break
        elif msg:
            sock.send(msg.encode('utf-8'))
 
 
def client_start():
    """クライアントのスタート"""
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    handle_thread = threading.Thread(target=handler, args=(sock,))
    handle_thread.daemon = True
    handle_thread.start()

    try:
        input_msg_roop(sock)
    finally:
        sock.close()
 
 
def handler(sock):
    """サーバからメッセージを受信し、表示する"""
 
    while True:
        data = sock.recv(1024)
        print("[受信]{}".format(data.decode("utf-8")))
 
 
if __name__ == "__main__":
    client_start()