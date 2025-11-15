# broadcast_receiver.py
import socket

PORT = 50000        # 브로드캐스트 메시지를 받을 포트
BUFFER_SIZE = 1024

# 1. UDP 소켓 생성
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 포트 재사용 및 브로드캐스트 수신 허용 옵션
receiver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # 2. 모든 인터페이스에서 해당 포트를 통해 수신하도록 바인딩
    # '0.0.0.0'은 모든 IP 주소로부터 수신하겠다는 의미
    receiver_socket.bind(('', PORT))
    print(f"✅ 브로드캐스트 수신 시작: 포트 {PORT}. 메시지 대기 중...")

    # 3. 데이터 수신 (무한 루프)
    while True:
        # 데이터와 송신자 주소(addr) 획득
        data, addr = receiver_socket.recvfrom(BUFFER_SIZE)
        
        # 💡 데이터 디코딩
        message = data.decode('utf-8')
        print(f"\n[수신자] ⬇️ 수신 from {addr[0]}: {message}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 4. 소켓 종료
    receiver_socket.close()
    print("🛑 수신자 소켓 종료.")