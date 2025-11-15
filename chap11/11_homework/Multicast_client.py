# multicast_sender.py
import socket

# =========================================================
# 멀티캐스트 그룹 설정 (수신자와 동일해야 함)
MCAST_GRP = '224.1.1.1' 
MCAST_PORT = 50007      
SERVER_ADDRESS = (MCAST_GRP, MCAST_PORT)

# 1. UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# 2. 💡 Windows 환경에서 송신 인터페이스 명시 (추가)
# --------------------------------------------------------------------------
# [!!!] '172.26.53.211'은 WSL2의 내부 IP이므로, Windows 송신 인터페이스로 사용 불가합니다.
# [!!!] 이 값 대신 Windows 호스트의 실제 LAN/WiFi 어댑터 IPv4 주소를 사용해야 합니다.
# --------------------------------------------------------------------------
# 예시: '192.168.1.10'을 실제 Windows IP로 변경
WINDOWS_REAL_IP = '172.26.48.1' 
try:
    MCAST_IF = socket.inet_aton(WINDOWS_REAL_IP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, MCAST_IF)
except OSError as e:
    print(f"❌ 설정 오류: IP 주소 '{WINDOWS_REAL_IP}'가 유효하지 않거나 사용 가능한 인터페이스가 아닙니다. ({e})")
    print("   -> Windows의 'ipconfig' 명령어로 실제 IP를 확인 후 코드를 수정하세요.")
    # 오류 발생 시 기본값으로 설정하여 통신 시도를 계속함 (권장하지 않음)
    # MCAST_IF = socket.inet_aton('0.0.0.0')
    # sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, MCAST_IF)
# =========================================================

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