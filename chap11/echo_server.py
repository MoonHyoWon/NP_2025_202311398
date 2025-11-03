from socket import *

PORT = 2500
BUFSIZE = 1024

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 포트 재사용
    sock.bind(('localhost', PORT))                # 종단점 주소 바인딩
    sock.listen(1)                                # 대기열 크기 1
    print(f"Listening on localhost:{PORT}")

    while True:
        conn, (remotehost, remoteport) = sock.accept()  # 연결 수락
        print('Connected by', remotehost, remoteport)
        with conn:
            while True:
                data = conn.recv(BUFSIZE)               # 데이터 수신(바이트)
                if not data:                            # 빈 바이트면 종료
                    break
                print("Received message:", data.decode(errors='ignore'))
                conn.sendall(data)                      # 에코(그대로 다시 전송)
        print("Connection closed")