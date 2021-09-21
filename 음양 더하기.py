def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # 양이면
        if signs[i]:
            answer += absolutes[i]
        # 음이면
        else:
            answer -= absolutes[i]
    return answer
