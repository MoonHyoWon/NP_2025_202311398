# import argparse
# parser = argparse.ArgumentParser() #명령 인자를 해석할 객체 생성 
# parser.add_argument('-s', default="127.0.0.1") #서버 인자 정의 
# parser.add_argument('-p', type=int, default=2500) #포트 인자 정의 
# args = parser.parse_args() #옵션값 저장
# sock.connect((args.s, args.p)) #서버와 포트 인자
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP")                        # ✅ 이름은 IP (문자열)
parser.add_argument("--port", "-p", type=int, default=2500)
args = parser.parse_args()

print("serverIP:", args.IP)
print("port:", args.port)
