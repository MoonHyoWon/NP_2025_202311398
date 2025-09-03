# 7. 문자열과 하나의 문자를 받아 문자열에서 그 문자가 위치를 모두 찾아 콘솔에 출력하고 그 갯수를 반환하는 함수 (예: Hello, l -> 2,3 출력하고 2를 반환)
# 학번 : 202311398
# 작성자 : 문효원

def find_num(st, char):
    check_find = 0
    for i in range(0, len(st)):
        if st[i] == char:
            check_find += 1
            print("일치하는 자리 : ", i)
    return check_find

st = input("문자열을 입력하시오. : ")
char = input("문자 하나를 입력하시오 : ")

print("일치하는 갯수 : ", find_num(st, char))