#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = 'localhost'
port = 50007

#オブジェクトの作成をします
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))
client.send("from rafael")

response = client.recv(4096)

print response