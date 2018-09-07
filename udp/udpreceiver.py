import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "localhost"
port = 5000
client.bind((host,port))

while True:
    data, addr = client.recvfrom(4096)
    print data
    time.sleep(1)
