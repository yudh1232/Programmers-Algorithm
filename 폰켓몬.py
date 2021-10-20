def solution(nums):
    # 1~200000에 대응되는 visited 리스트 생성
    visited = [False] * 200001
    
    # 다른 숫자의 개수 변수
    count = 0
    
    # 다른 숫자의 개수를 셈
    for n in nums:
        if visited[n] == False:
            visited[n] = True
            count += 1
    
    # 결과값 변수
    answer = 0
    
    # 다른 숫자의 개수가 N/2마리 이상이라면
    if count >= len(nums) // 2:
        # 답은 N/2마리
        answer = len(nums) // 2
    # 다른 숫자의 개수가 N/2마리 보다 작다면
    else:
        # 답은 다른 숫자의 개수
        answer = count

    # 결과 리턴
    return answer
