def solution(N, stages):
    # 전체 유저 수
    total = len(stages)
    
    # 스테이지별 유저 수 리스트 생성
    user_count = [0] * (N + 2)
    
    # 스테이지별 유저 수 계산
    for stage in stages:
        user_count[stage] += 1
    
    # 스테이지별 실패율 리스트 생성
    failure_rate = []
    
    # 스테이지별 실패율 계산
    for i in range(1, N + 1):
        # 도달한 사람이 없는 스테이지는 실패율이 0
        if total == 0:
            failure_rate.append((i, 0))
        else:
            # 실패율: 머물러있는 사람 / 현재 스테이지에 도달한 사람
            failure_rate.append((i, user_count[i] / total))
            # 다음 스테이지로 가기 전 머물러있는 사람 수를 뺌
            total -= user_count[i]
    
    # 실패율의 내림차순으로 정렬
    failure_rate.sort(key = lambda x: -x[1])
    
    # 결과 리스트 생성
    answer = []
    
    # 실패율의 내림차순으로 스테이지의 번호를 결과 리스트에 넣음
    for f in failure_rate:
        answer.append(f[0])
    
    # 결과 리턴
    return answer
