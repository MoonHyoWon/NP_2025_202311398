# 9. 두 개의 3x3 행렬을 입력받아 행렬덧셈 결과행렬을 반환하는 함수
# 학번 : 202311398
# 작성자 : 문효원

def matrix_sum(m1, m2):
    m3= [
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(2):
        for j in range(3):
            m3[i][j] = m1[i][j] + m2[i][j]
    
    return m3

def input_matrix():
    m = [
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(2):
        for j in range(3):
            m[i][j] = int(input("정수를 입력하시오 : "))

    return m

print("============ 첫 번째 행렬 생성 ============")
matrix1 = input_matrix()
print("============ 두 번째 행렬 생성 ============")
matrix2 = input_matrix()

print("첫 번째 행렬 : ", matrix1)
print("두 번째 행렬 : ", matrix2)
print("덧셈한 결과 : ", matrix_sum(matrix1, matrix2))
