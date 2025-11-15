import socket
port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))
while True: #무한 루프 실행
    print("<- ", end ='')
    data, addr = sock.recvfrom(BUFFSIZE) #수신 메시지 출력 
    print(data.decode())
    resp = input("-> ") #송신 메시지 입력
    sock.sendto(resp.encode(),addr) #입력 메시지 송신