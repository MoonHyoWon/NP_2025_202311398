# tcp_echo_server.py
import socket

# 서버 설정 (localhost)
HOST = '127.0.0.1' 
PORT = 65432        
BUFFER_SIZE = 1024  # 수신할 데이터의 최대 크기

# 1. TCP 소켓 생성 및 옵션 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # 2. 바인딩 및 연결 대기 (listen)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"✅ 서버 시작: {HOST}:{PORT}. 클라이언트 연결 대기 중...")

    # 3. 연결 수락 (3-Way Handshake 완료)
    conn, addr = server_socket.accept()
    print(f"🤝 클라이언트 연결됨: {addr}")

    # 4. 데이터 통신 및 에코 기능 구현
    while True:
        # 데이터 수신 (바이트열 형태)
        data = conn.recv(BUFFER_SIZE)
        if not data:
            print(f"💔 클라이언트 {addr} 연결 종료.")
            break
        
        # 💡 이기종 호환성: 바이트열을 UTF-8 문자열로 디코딩
        message = data.decode('utf-8')
        print(f"⬇️ 수신: {message}")

        # 응답 메시지 준비
        response = f"[ECHO from S] {message}"
        
        # 💡 이기종 호환성: 문자열을 UTF-8 바이트열로 인코딩하여 전송
        conn.sendall(response.encode('utf-8'))
        print(f"⬆️ 송신: {response}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 5. 소켓 종료 (4-Way Handshake 시작)
    if 'conn' in locals():
        conn.close()
    server_socket.close()
    print("🛑 서버 소켓 종료.")