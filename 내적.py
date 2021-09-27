def solution(a, b):
    answer = 0
    
    # 내적 계산
    for i in range(len(a)):
        answer += a[i] * b[i]

    # 결과 리턴
    return answer
