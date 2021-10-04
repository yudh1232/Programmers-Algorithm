def rotate(matrix, q):
    x1, y1, x2, y2 = q

    # 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자 변수
    min_value = 10000

    # 회전을 위해 temp 변수 이용 
    temp = matrix[x1][y1]
    min_value = min(min_value, temp)

    # 테두리 회전 및 min_value 갱신
    for i in range(x1, x2):
        matrix[i][y1] = matrix[i + 1][y1]
        min_value = min(min_value, matrix[i][y1])
    for i in range(y1, y2):
        matrix[x2][i] = matrix[x2][i + 1]
        min_value = min(min_value, matrix[x2][i])
    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i - 1][y2]
        min_value = min(min_value, matrix[i][y2])
    for i in range(y2, y1, -1):
        matrix[x1][i] = matrix[x1][i - 1]
        min_value = min(min_value, matrix[x1][i])
    
    matrix[x1][y1 + 1] = temp

    return min_value


def solution(rows, columns, queries):
    # matrix 리스트 생성
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = num
            num += 1

    answer = []

    # 각 쿼리에 대하여
    for q in queries:
        # matrix를 회전하고 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자를 구함
        min_value = rotate(matrix, q)
        answer.append(min_value)

    # 결과 리턴
    return answer
