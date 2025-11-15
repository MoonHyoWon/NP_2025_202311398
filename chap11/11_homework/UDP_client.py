# udp_echo_client_user_input.py
import socket

# 서버 설정
HOST = '172.26.53.211'  # 서버의 IP 주소
PORT = 65432        # 서버의 포트 번호
SERVER_ADDRESS = (HOST, PORT)
BUFFER_SIZE = 1024

# 1. UDP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print(f"✅ UDP 클라이언트 시작. 서버: {HOST}:{PORT}")
    print("메시지를 입력하고 엔터를 누르세요. ('quit' 입력 시 종료)")

    # 2. 데이터 통신 (사용자 입력 루프)
    while True:
        # 사용자로부터 메시지 입력 받기
        user_input = input(">> ")
        
        if user_input.lower() == 'quit':
            break

        # 💡 이기종 호환성: 인코딩 후, 서버 주소로 sendto()
        client_socket.sendto(user_input.encode('utf-8'), SERVER_ADDRESS)
        print(f"[클라이언트] ⬆️ 송신: {user_input}")

        # 서버 응답 수신 및 송신자 주소(server_addr) 획득
        data, server_addr = client_socket.recvfrom(BUFFER_SIZE)
        
        # 💡 이기종 호환성: 디코딩
        response = data.decode('utf-8')
        print(f"[클라이언트] ⬇️ 수신 from {server_addr}: {response}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 3. 소켓 종료
    client_socket.close()
    print("\n🛑 UDP 클라이언트 소켓 종료.")