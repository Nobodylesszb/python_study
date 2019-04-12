# 服务端
from socket import socket

server = socket()
server.bind(('127.0.0.1',7000))
server.listen(5)
while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        conn.send(data.upper())
    conn.close()
server.close()


