import socket

s = socket.socket()
print('socket created')
s.bind(('localhost',9999))

s.listen(3)
print('Waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Connected with', addr, name)
    if(name != 'teja'):
        c.send(bytes('who the fuck are you, I am looking for teja','utf-8'))
    else: c.send(bytes('welcome bro','utf-8'))
    c.close()