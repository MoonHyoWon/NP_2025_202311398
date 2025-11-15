from socket import *

SERVER = '127.0.0.1'  # 서버 IP로 변경
PORT = 2500           # 서버 포트로 변경
BUFFER = 1024

def main():
    # UDP 소켓 생성
    c_sock = socket(AF_INET, SOCK_DGRAM)
    c_sock.connect((SERVER, PORT))

    for i in range(10):  # 10번 시도
        delay = 0.1      # 각 시도마다 0.1초부터 시작
        data = 'Hello message'

        while True:
            # 메시지 전송
            c_sock.send(data.encode())
            print(f'[{i+1}] Waiting up to {delay} seconds for a reply')

            # 타임아웃 설정
            c_sock.settimeout(delay)

            try:
                # 응답 대기
                recv_data = c_sock.recv(BUFFER)
            except timeout:
                # 타임아웃 시 대기 시간 2배 증가
                delay *= 2
                if delay > 2.0:
                    print(f'[{i+1}] No response (timeout > 2.0s). Giving up this try.')
                    break  # 이 시도 포기하고 다음 i로
            else:
                # 응답 받으면 출력 후 다음 i로
                print('Response:', recv_data.decode())
                break

    c_sock.close()

if __name__ == "__main__":
    main()
