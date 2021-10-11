def solution(answers):    
    # 1번, 2번, 3번의 찍는 방식
    data1 = [1, 2, 3, 4, 5] # 5를 주기로 순환
    data2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8을 주기로 순환
    data3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10을 주기로 순환

    # 1번, 2번, 3번의 점수
    count1, count2, count3 = 0, 0, 0

    # 1번, 2번, 3번의 점수 계산
    for i in range(len(answers)):
        if data1[i % 5] == answers[i]:
            count1 += 1
        if data2[i % 8] == answers[i]:
            count2 += 1
        if data3[i % 10] == answers[i]:
            count3 += 1
    
    # 결과 리스트 생성
    answer = []
    if count1 == count2:
        if count2 == count3:
            answer = [1, 2, 3]
        elif count2 > count3:
            answer = [1, 2]
        else:
            answer = [1, 3]
    elif count1 > count2:
        if count1 == count3:
            answer = [1, 3]
        elif count1 > count3:
            answer = [1]
        else:
            answer = [3]
    else:
        if count2 == count3:
            answer = [2, 3]
        elif count2 > count3:
            answer = [2]
        else:
            answer = [3]
    
    # 결과 리턴
    return answer
