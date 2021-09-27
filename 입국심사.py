def solution(n, times):
    # 이진탐색을 위한 left와 right 초기값 설정
    min_time = min(times)
    left = 1
    right = n * min_time

    # 이진탐색
    while left <= right:
        # middle 구하기, middle: 시간
        middle = (left + right) // 2

        # middle을 기준으로 몇명의 입국심사를 처리할 수 있는지 구함
        count = 0
        for t in times:
            count += middle // t
        
        # n명이상 처리할 수 있으면 right를 낮춤
        if count >= n:
            right = middle - 1
        # n명이상 처리할 수 없으면 left를 높임
        else:
            left = middle + 1

    # 결과 리턴
    return left
