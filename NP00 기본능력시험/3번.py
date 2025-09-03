# 3. 두 수 a,b를 입력받아 다음 계산을 하는 함수
# a+b, a << b, a * b를 계산하여 콘솔에 출력하고 후 그 중 가장 큰 값을 반환
# 학번 : 202311398
# 작성자 : 문효원

def Calculation(a, b):
    num1 = a + b
    print("a + b = ", num1)

    num2 = a << b
    print("a << b = ", num2)

    num3 = a * b
    print("a * b = ", num3)

    return max(num1, num2, num3)

a = int(input("정수를 입력하시오 : "))
b = int(input("정수를 입력하시오 : "))
num1 = Calculation(a,b)

print("가장 큰 값 : ", num1)
