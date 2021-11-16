def solution(d, budget):
    answer = 0
    
    # d를 오름차순으로 정렬
    d.sort()
    
    # d를 순회
    for money in d:
        # 현재 부서의 신청금액이 budget보다 크다면 반복종료
        if money > budget:
            break
        
        # budget에서 현재 부서의 신청금액을 뺌
        budget -= money
        # 지원횟수 증가
        answer += 1
    
    # 결과 리턴
    return answer
