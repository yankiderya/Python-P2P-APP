from socket import *
import socket
import time
import os
import json
username=input("Please enter your username: ") +":"
userip = socket.gethostbyname(socket.gethostname())


while 1:
    s = socket.socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    ldir = os.getcwd() + '/chunks'
    if not os.path.exists(os.getcwd() + '/Received Files'):
        os.makedirs(os.getcwd() + '/Received Files')
    receiveddir=os.getcwd() + '/Received Files'
    files = os.listdir(receiveddir)
    chunks = os.listdir(ldir)
    x = {
        "username": username+userip,
        "chunks": chunks,
        "files":files


    }
    y = json.dumps(x)
    s.sendto(y.encode('utf-8'), ('25.255.255.255', 5000))
    time.sleep(60)

