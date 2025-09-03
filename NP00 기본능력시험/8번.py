# 8. 두 개의 자연수를 입력받아 그 두 수 사이의 홀수만을 더해서 반환하는 함수 (단, 그 두 수도 포함)
# 학번 : 202311398
# 작성자 : 문효원

def odd_sum(a, b):
    sum = a
    for i in range(a+1, b-1):
        if i % 2 != 0:
            sum += i
    sum += b
    return sum

a = int(input("정수를 입력하시오 : "))
b = int(input("정수를 입력하시오 : "))

print("두 수 사이의 홀수 합(두 수 포함) : ", odd_sum(a, b))