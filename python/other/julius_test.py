import socket
import string

def main() :
  host = '192.168.116.192'
  port = 10500

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))

  data = ""
  while True:

    while (string.find(data, "\n.") == -1):
      data = data + sock.recv(1024)

    strTemp = ""
    for line in data.split('\n'):
      index = line.find('WORD="')
      if index != -1:
        line = line[index + 6:line.find('"', index + 6)]
        if line != "[s]":
          strTemp = strTemp + line

    if strTemp != "":
      print("result:" + strTemp)

    data = ""

if __name__ == "__main__":
  main()