import socket
import sys
import time
import os

s=socket.socket()
host = socket.gethostname()
port = 8080
host = socket.gethostname()
print("waiting for connections...")
s.bind(('0.0.0.0', 9990))
s.listen(5)
conn, addr = s.accept()
print(addr, "is connected to server")

while True:
    command = input(str("Enter Command :"))
    conn.send(command.encode())
    print("Command has been sent successfully.")
    data = conn.recv(1024)
