#!usr/bin/python
from socket import *
import subprocess
 
host = 'localhost' # '127.0.0.1' can also be used
port = 52000
 
sock = socket()
#Connecting to socket
sock.connect((host, port)) #Connect takes tuple of host and port
 
#Infinite loop to keep client running.
while True:
    data = sock.recv(1024)
    if (data == 'Hi'):
      subprocess.call(["shutdown", "/s"])
 
sock.close()