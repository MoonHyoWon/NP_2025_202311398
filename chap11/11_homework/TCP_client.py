# tcp_echo_client_user_input.py
import socket

# 서버 설정
HOST = '127.0.0.1'  # 서버의 IP 주소로 변경 (테스트 시엔 localhost)
PORT = 65432        # 서버의 포트 번호
BUFFER_SIZE = 1024

# 1. TCP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 2. 서버 연결 요청 (3-Way Handshake)
    client_socket.connect((HOST, PORT))
    print(f"✅ 서버에 연결됨: {HOST}:{PORT}")
    print("메시지를 입력하고 엔터를 누르세요. ('quit' 입력 시 종료)")

    # 3. 데이터 통신 (사용자 입력 루프)
    while True:
        # 사용자로부터 메시지 입력 받기
        user_input = input(">> ")
        
        if user_input.lower() == 'quit':
            break

        # 💡 이기종 호환성: 문자열을 UTF-8 바이트열로 인코딩하여 전송
        client_socket.sendall(user_input.encode('utf-8'))
        print(f"[클라이언트] ⬆️ 송신: {user_input}")

        # 서버 응답 수신
        data = client_socket.recv(BUFFER_SIZE)
        if data:
            # 💡 이기종 호환성: 바이트열을 UTF-8 문자열로 디코딩
            response = data.decode('utf-8')
            print(f"[클라이언트] ⬇️ 수신: {response}")
        else:
            print("[클라이언트] 서버가 연결을 종료했습니다.")
            break

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 4. 소켓 종료 (4-Way Handshake 시작)
    client_socket.close()
    print("\n🛑 클라이언트 소켓 종료.")