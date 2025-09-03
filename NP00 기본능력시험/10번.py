# 10. 학번이 문자열로 주어지면 입학년도를 정수로 반환하는 함수
# 학번 : 202311398
# 작성자 : 문효원

def change_int(sn):
    num = 0
    for i in range(4):
        num += int(sn[i])*10**(3-i)
    # num = int(sn[0]) *1000 + int(sn[1])*100 + int(sn[2]) + int(sn[3])
    return num

sn = input("학번을 입력하시오. : ")
print("입학한 날짜 : ", change_int(sn))