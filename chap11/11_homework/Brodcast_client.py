# broadcast_sender.py
import socket

PORT = 50000              # 수신자가 대기하는 포트와 일치해야 함
BROADCAST_ADDR = '172.26.53.211' # 전송할 브로드캐스트 주소 (로컬 서브넷 전체)
SERVER_ADDRESS = (BROADCAST_ADDR, PORT)

# 1. UDP 소켓 생성
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 💡 브로드캐스트 전송을 명시적으로 허용하는 옵션 설정 (필수!)
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

try:
    print(f"✅ 브로드캐스트 송신 시작. 대상: {BROADCAST_ADDR}:{PORT}")
    print("메시지를 입력하고 엔터를 누르세요. ('quit' 입력 시 종료)")

    # 3. 데이터 전송 (사용자 입력 루프)
    while True:
        user_input = input(">> ")
        
        if user_input.lower() == 'quit':
            break

        # 💡 문자열 인코딩 후 브로드캐스트 주소로 sendto()
        sender_socket.sendto(user_input.encode('utf-8'), SERVER_ADDRESS)
        print(f"[송신자] ⬆️ 브로드캐스트 송신: {user_input}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 4. 소켓 종료
    sender_socket.close()
    print("\n🛑 송신자 소켓 종료.")