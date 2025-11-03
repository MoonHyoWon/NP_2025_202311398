# echo_client.py
import socket

BUFSIZE = 1024

def main():
    try:
        port = int(input("Port No: ").strip())
    except ValueError:
        print("포트 번호는 정수여야 합니다.")
        return

    address = ("localhost", port)  # 서버 주소와 포트 번호

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(address)  # 서버 연결 요청
            print(f"Connected to {address[0]}:{address[1]}")
            print("메시지를 입력하세요. 종료하려면 'quit' 또는 'exit' 입력.")
        except OSError as e:
            print(f"서버에 연결할 수 없습니다: {e}")
            return

        try:
            while True:
                msg = input("Message to send: ")

                # 종료 명령
                if msg.strip().lower() in ("quit", "exit"):
                    print("클라이언트를 종료합니다.")
                    break

                # 빈 입력은 전송하지 않음
                if not msg:
                    continue

                # 메시지 전송
                s.sendall(msg.encode("utf-8"))

                # 서버로부터 수신
                data = s.recv(BUFSIZE)
                if not data:
                    print("서버가 연결을 종료했습니다.")
                    break

                print("Received message:", data.decode("utf-8", errors="ignore"))
        except KeyboardInterrupt:
            print("\n사용자 중지로 종료합니다.")

if __name__ == "__main__":
    main()