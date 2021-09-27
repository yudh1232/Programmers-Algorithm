import heapq

def solution(scoville, K):
    answer = 0 # 섞은 횟수

    # min-heap 사용
    heapq.heapify(scoville)

    # scoville의 원소가 2개 이상일 경우 반복
    while len(scoville) >= 2:
        # 가장 작은 값이 K이상이면 결과 리턴
        if scoville[0] >= K:
            return answer

        # 가장 작은 값과 두번째로 작은 값을 섞어 heap에 넣음
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
        
        # 섞은 횟수 증가
        answer += 1

    # scoville의 원소가 1개일 때, 남은 1개의 값이 K이상이면
    if scoville[0] >= K:
        return answer
    # K보다 작으면
    else:
        return -1
