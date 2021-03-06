def solution(lines):
    log = [] # 요청의 시작시간과 끝시간을 담는 리스트

    # 인풋에 대해 시간을 정수로 변환, log에 요청의 시작시간과 끝시간을 넣음
    for i in lines:
        h = int(i[11:13])
        m = int(i[14:16])
        s = int(i[17:19])
        ms = int(i[20:23])
        t = int(float(i[24:-1]) * 1000)

        end_value = h * 60 * 60 * 1000 + m * 60 * 1000 + s * 1000 + ms
        start_value = end_value - t + 1

        # 요청의 시작시간과 끝시간을 넣음
        log.append((start_value, end_value))

    # 결과값
    answer = 0

    # 각 요청에 대해
    for i in range(len(log)):
        count = 1 # [끝시간, 끝시간 + 999] 범위의 처리 수

        # (i + 1)부터의 요청에 대해
        for j in range(i + 1, len(log)):

            # log[j]가 log[i]의 [끝시간, 끝시간 + 999] 범위와 만난다면
            if log[i][1] + 999 < log[j][0]:
                continue
            else:
                count += 1
        
        # 결과값 갱신
        answer = max(answer, count)

    return answer
