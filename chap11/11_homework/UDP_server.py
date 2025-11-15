# udp_echo_server.py
import socket

HOST = '127.0.0.1'  # 서버 IP
PORT = 65432        # 사용할 포트 번호
BUFFER_SIZE = 1024

# 1. UDP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # 2. 바인딩
    server_socket.bind((HOST, PORT))
    print(f"✅ UDP 서버 시작: {HOST}:{PORT}. 데이터 수신 대기 중...")

    # 3. 데이터 통신 (무한 루프)
    while True:
        # 데이터 수신 및 송신자 주소(addr) 획득
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        
        # 💡 이기종 호환성: 디코딩
        message = data.decode('utf-8')
        print(f"\n⬇️ 수신 from {addr}: {message}")

        # 에코(Echo) 응답 준비
        response = f"[ECHO from S] {message}"
        
        # 💡 이기종 호환성: 인코딩 후, 클라이언트 주소로 sendto()
        server_socket.sendto(response.encode('utf-8'), addr)
        print(f"⬆️ 송신 to {addr}: {response}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 4. 소켓 종료
    server_socket.close()
    print("🛑 UDP 서버 소켓 종료.")