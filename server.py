#Server side Networking
import socket

host = '127.0.0.1'
port = 10000 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
c, addr = s.accept()
print("The client got connected")

c.send(b"Hello Client, are you doing well?")
str = "Bye...!"
c.send(str.encode())

s.close()
c.close()
