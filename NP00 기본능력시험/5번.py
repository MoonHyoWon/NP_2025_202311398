# 5. 두 정수 n부터 m까지 1씩 증가하면서 숫자를 합한 결과를 출력하는 함수 (n과 m 포함)
# 학번 : 202311398
# 작성자 : 문효원

def num2sum(n, m):
    sum = 0
    for i in range(n, m+1):
        sum = sum + i
    return sum

n = int(input("정수를 입력하시오 : "))
m = int(input("정수를 입력하시오 : "))

print("합한 결과 = ", num2sum(n, m))