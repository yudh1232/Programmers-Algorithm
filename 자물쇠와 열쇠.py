from copy import deepcopy

# 행렬을 시계방향으로 90도 회전
def rotate_90(key, m):
    temp = deepcopy(key)
    for i in range(m):
        for j in range(m):
            key[j][m - 1 - i] = temp[i][j]

def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 계산하기 쉽게 자물쇠를 3배로 확장
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]

    # new_lock의 가운데 부분에 원래 자물쇠를 넣음
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 회전을 4번하면 원래대로 돌아오므로 4번 반복
    for _ in range(4):
        # 키를 회전
        rotate_90(key, m)

        # 한칸씩 이동하면서 키를 자물쇠에 꽂아봄
        for i in range(n - m, 2 * n + 1):
            for j in range(n - m, 2 * n + 1):
                for a in range(m):
                    for b in range(m):
                        # 키를 꽂음
                        new_lock[i + a][j + b] += key[a][b]
                
                # 키가 딱 맞는지 체크
                flag = True
                for a in range(n):
                    for b in range(n):
                        if new_lock[n + a][n + b] != 1:
                            flag = False
                # 키가 딱 맞으면
                if flag == True:
                    return True

                # 키가 딱 안 맞았으면 키를 뺌
                for a in range(m):
                    for b in range(m):
                        new_lock[i + a][j + b] -= key[a][b]

    # 모든경우에 대하여 키가 안맞았으면
    return False
