import socket
import random

port = 2500
BUFFSIZE = 1024

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')
while True:
    data, address = s_sock.recvfrom(BUFFSIZE) 
    if random.randint(1, 10) < 4: #30% 데이터 손실 가정
        print('Packet from {} lost!!!'.format(address)) 
        continue #응답하지 않음
    print('Message is {!r} from {}'.format(data.decode(), address)) #정상 수신 메시지 
    s_sock.sendto('ACK'.encode(), address) #ACK 응답 전송