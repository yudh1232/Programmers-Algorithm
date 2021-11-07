def solution(x, n):
    answer = []
    
    # 초기값 설정
    data = x
    
    # n만큼 반복
    for _ in range(n):
        # data를 answer 리스트에 넣음
        answer.append(data)
        # data를 x만큼 증가
        data += x
    
    # 결과 리턴
    return answer
