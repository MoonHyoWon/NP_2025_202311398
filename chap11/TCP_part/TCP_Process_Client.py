# TCP_Process_Client.py
import socket

HOST = '127.0.0.1'   # 서버 주소 (동일 PC면 localhost)
PORT = 2500          # 서버 포트 (서버 코드와 동일)
BUFSIZE = 1024

def main():
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as s:
            print(f"Connected to {HOST}:{PORT}")
            print("1~10 사이 숫자를 입력하세요. 종료하려면 'quit' 또는 'exit' 입력.")
            while True:
                msg = input("Number> ").strip()
                if not msg:
                    continue

                # 종료 명령
                if msg.lower() in ("quit", "exit"):
                    s.sendall(msg.encode("utf-8"))
                    # 서버가 'Bye'를 보내면 출력하고 종료
                    resp = s.recv(BUFSIZE)
                    if resp:
                        print(resp.decode("utf-8", errors="ignore"), end="")
                    print("클라이언트를 종료합니다.")
                    break

                # 메시지 전송
                s.sendall(msg.encode("utf-8"))

                # 응답 수신
                data = s.recv(BUFSIZE)
                if not data:
                    print("서버가 연결을 종료했습니다.")
                    break
                print("Server:", data.decode("utf-8", errors="ignore"), end="")

    except (ConnectionRefusedError, TimeoutError, OSError) as e:
        print(f"서버에 연결할 수 없습니다: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n사용자 취소로 종료합니다.")