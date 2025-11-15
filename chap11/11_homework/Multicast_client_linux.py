# multicast_sender.py
import socket

# 멀티캐스트 그룹 설정 (수신자와 동일해야 함)
MCAST_GRP = '224.1.1.1' 
MCAST_PORT = 50007      
SERVER_ADDRESS = (MCAST_GRP, MCAST_PORT)

# 1. UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

try:
    print(f"✅ 멀티캐스트 송신 시작. 대상 그룹: {MCAST_GRP}:{MCAST_PORT}")
    print("메시지를 입력하고 엔터를 누르세요. ('quit' 입력 시 종료)")

    # 2. 데이터 전송 (사용자 입력 루프)
    while True:
        user_input = input(">> ")
        
        if user_input.lower() == 'quit':
            break

        # 💡 인코딩 후 멀티캐스트 그룹 주소로 sendto()
        sock.sendto(user_input.encode('utf-8'), SERVER_ADDRESS)
        print(f"[송신자] ⬆️ 멀티캐스트 송신: {user_input}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 3. 소켓 종료
    sock.close()
    print("\n🛑 송신자 소켓 종료.")