#Server side basic program
import socket

host = '127.0.0.1'
port = 10000 #Let it be b/w  10k to 50 k

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
c, addr = s.accept()
print("The client got connected")

c.send(b"Hello Client, are you the Velagala")
c.send(b"Just go to Bhavana, you Mr.Peice of Shit")
str = "Get Lost...!"
c.send(str.encode())

s.close()
c.close()
