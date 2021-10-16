def solution(n, lost, reserve):
    answer = 0
    
    # 여벌의 체육복을 가져왔지만 체육복을 도난당한 학생 케이스 처리
    new_reserve = [] # 새로운 여벌 체육복 리스트 생성
    
    # 기존의 여벌 체육복 중에서
    for r in reserve:
        # lost에 있다면
        if r in lost:
            lost.remove(r) # lost에서 제거하고 새로운 여벌 체육복에 안넣음
        # lost에 없다면
        else:
            new_reserve.append(r) # 새로운 여벌 체육복에 넣음
    
    # lost를 정렬
    lost.sort()
    
    # 1부터 n까지 살핌
    for i in range(1, n + 1):
        # i가 lost에 있다면
        if i in lost:
            # i의 앞번호에 여벌이 있다면
            if i - 1 in new_reserve:
                # i는 체육수업을 들을 수 있다
                answer += 1
                # 앞번호의 여벌 제거
                new_reserve.remove(i - 1)
            # i의 앞번호에는 여벌이 없고 뒷번호에 있다면    
            elif i + 1 in new_reserve:
                # i는 체육수업을 들을 수 있다
                answer += 1
                # 뒷번호의 여벌 제거
                new_reserve.remove(i + 1)
        # i가 lost에 없다면
        else:
            answer += 1 # i는 체육수업을 들을 수 있다
    
    # 결과 리턴
    return answer
