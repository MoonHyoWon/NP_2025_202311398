# multicast_receiver.py
import socket
import struct

# 멀티캐스트 그룹 설정
MCAST_GRP = '224.1.1.1' # 사용할 멀티캐스트 IP 주소
MCAST_PORT = 50007      # 사용할 포트 번호
BUFFER_SIZE = 1024

# 1. UDP 소켓 생성 및 바인딩
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # 2. 멀티캐스트 그룹 IP와 포트에 바인딩
    sock.bind(('', MCAST_PORT)) 
    
    # 3. 💡 그룹 가입 (IP_ADD_MEMBERSHIP)
    mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    print(f"✅ 멀티캐스트 수신 시작: 그룹 {MCAST_GRP}:{MCAST_PORT} 가입 완료.")

    # 4. 반복 수신
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message = data.decode('utf-8')
        print(f"\n[수신자] ⬇️ 수신 from {addr[0]}: {message}")

except Exception as e:
    print(f"❌ 오류 발생: {e}")

finally:
    # 5. 💡 그룹 탈퇴 (IP_DROP_MEMBERSHIP)
    mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
    sock.close()
    print("🛑 수신자, 그룹 탈퇴 및 소켓 종료.")