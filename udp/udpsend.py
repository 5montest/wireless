import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "localhost"
port = 5000

while True:
    client.sendto("Hello!",(host,port))
    print "send"
    time.sleep(1)

