# 客户端

from socket import socket
client = socket()
client.bind(('127.0.0.1',7000))

while True:
    msg = input('>>>').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024).decode('uft-8')
    print('服务端已接受客服端的数据并转化为大写', data)
     
client.close()

