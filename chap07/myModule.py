# myModule.py

def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def power(x, n):
    prod = 1
    for i in range(1, n+1):
        prod *= x
    return prod

if __name__ == '__main__':  # myModule.py를 직접 실행할 때만 아래 코드 실행
    print(sum(5))
    print(power(2, 3))