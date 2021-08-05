import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('wating for connection')

while True:
   c, adress = s.accept()
   print("Connected with", adress)

   c.send("Welcome to Theconbox")