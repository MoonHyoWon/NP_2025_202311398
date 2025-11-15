# TCP_Process_Server.py
import socket

# 숫자 문자열 -> 영어 단어 매핑
TABLE = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
    '9': 'nine', '10': 'ten'
}

HOST = '127.0.0.1'       
# HOST = ""        # 빈 문자열이면 모든 인터페이스(0.0.0.0)
PORT = 2500
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Waiting... (listening on {HOST or '0.0.0.0'}:{PORT})")

    c_socket, c_addr = s.accept()
    print("Connection from", c_addr)

    with c_socket:
        while True:
            data = c_socket.recv(BUFSIZE)
            if not data:
                # 클라이언트가 연결 종료
                break

            key = data.decode("utf-8", errors="ignore").strip()
            if key.lower() in ("quit", "exit"):
                c_socket.sendall(b"Bye\r\n")
                break

            resp = TABLE.get(key)
            if resp is None:
                c_socket.sendall(b"Try again\r\n")
            else:
                c_socket.sendall((resp + "\r\n").encode("utf-8"))

    print("Connection closed")