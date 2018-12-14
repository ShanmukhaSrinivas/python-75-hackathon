#Client side basic program
import socket

host = "127.0.0.1"
port = 10000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
str = s.recv(2048)

while str:
    print(str)
    str = s.recv(2048)
s.close()
