import socket
from contextlib import closing
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 5000

sock.connect((host, port))
sock.send("Connected!")
while True:
    print host, sock.recv(4096)

