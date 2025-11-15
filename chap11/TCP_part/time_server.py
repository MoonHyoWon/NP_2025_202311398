import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 5000)
# address = ('localhost', 5000)
s.bind(address)
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connection requested from", addr)
    client.send(time.ctime(time.time()).encode())
    client.close()