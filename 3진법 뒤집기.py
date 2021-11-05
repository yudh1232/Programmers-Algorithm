def solution(n):
    # 스택 생성
    stack = []

    # n을 3으로 나눈 나머지들을 스택에 넣음
    while n > 0:
        stack.append(n % 3)
        n = n // 3

    answer = 0
    count = 0  # 자리수
    
    # 스택에서 꺼내면서 n(3진법)을 뒤집음
    while stack:
        # 각 자리의 숫자에 (3 ** 자리수)를 곱해서 answer에 더함
        answer += stack.pop() * (3 ** count)
        count += 1  # 자리수 증가

    # 결과 리턴
    return answer
