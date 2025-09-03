# 6. 하나의 십진수 정수가 주어지면 각 자리의 십진수의 합을 반환하는 함수를 작성 (예: 274 입력 --> 2+7+4 = 13 반환)
# 학번 : 202311398
# 작성자 : 문효원

def result(a):
    sum = 0
    while(a > 0):
        sum = sum + int(a % 10)
        a = a / 10
    return sum

a = int(input("정수를 입력하시오 : "))
print("각 자리의 합 = ", result(a))