import heapq

def solution(jobs):
    answer = 0
    
    # 힙 생성
    heap = []
    
    # jobs를 정렬
    jobs.sort()

    # 시간 변수
    t = 0

    # 각 작업에 대하여
    for i in range(len(jobs)):
        # 작업의 시작시간이 현재 시간이하이면
        if jobs[i][0] <= t:
            # 힙에 넣음
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
        # 작업의 시작시간이 현재 시간이하가 아니면
        else:
            # 힙이 비어있지 않으면
            if len(heap) != 0:
                while heap:
                    # 힙에서 작업을 꺼내서 처리
                    a, b = heapq.heappop(heap)
                    # 시간을 업데이트
                    t += a
                    answer += (t - b)

                    # 업데이트된 시간에 의해 작업이 힙에 들어갈 수 있으면
                    if jobs[i][0] <= t:
                        # 힙에 넣고 while문 종료
                        heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
                        break

            # 힙이 비어있으면(원래 비어있었거나, 위 while문을 지나서도 작업을 힙에 넣지 못한 경우) 
            if len(heap) == 0:
                # 시간을 업데이트, 힙에 넣음
                t = jobs[i][0]
                heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
    
    # 위에서 작업을 다 살펴본 후, 힙에 남아있는 작업들을 처리
    while heap:
        # 힙에서 작업을 꺼내서 처리
        a, b = heapq.heappop(heap)
        # 시간을 업데이트
        t += a
        answer += (t - b)
    
    # 평균을 구함
    answer //= len(jobs)
    
    # 결과 리턴
    return answer
