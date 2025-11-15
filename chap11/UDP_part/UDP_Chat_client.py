import socket

SERVER_IP = "172.26.53.211"  # 서버가 같은 PC면 그대로 두면 됨
PORT = 2500
BUFFSIZE = 1024

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_addr = (SERVER_IP, PORT)

    while True:
        msg = input("-> ")
        if not msg:
            continue
        if msg.lower() in ("q", "quit", "exit"):
            print("클라이언트 종료")
            break

        # 서버로 메시지 전송
        sock.sendto(msg.encode(), server_addr)

        try:
            # 서버 응답 대기
            data, addr = sock.recvfrom(BUFFSIZE)
        except ConnectionResetError:
            print("[에러] 서버가 응답하지 않거나 포트가 열려 있지 않습니다.")
            print(" - 서버 실행 여부, IP, 포트(2500) 확인해봐.")
            break

        print("<-", data.decode())

    sock.close()

if __name__ == "__main__":
    main()
