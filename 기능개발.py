def solution(progresses, speeds):
    answer = []

    length = len(progresses)
    
    # 기능 리스트를 순회하는데 쓰는 인덱스
    index = 0

    while index < length:
        # 오늘 완료된 기능의 수
        count = 0
        
        # 각 기능에 진도를 더함
        for i in range(length):
            progresses[i] += speeds[i]
        
        while True:
            # 개발이 완료된 기능이면 
            if progresses[index] >= 100:
                count += 1
                index += 1
                # 기능 리스트를 모두 순회했다면
                if index == length:
                    break
            # 개발이 완료되지 않은 기능이면
            else:
                break
        
        # 오늘 기능개발이 완료된 것이 있다면
        if count != 0:
            answer.append(count)

    # 결과 리턴
    return answer
