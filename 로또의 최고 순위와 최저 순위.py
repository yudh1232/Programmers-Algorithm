def solution(lottos, win_nums):
    # lottos에 있는 0의 개수
    zero_count = 0

    # lottos와 win_nums의 겹치는 숫자의 개수
    same_count = 0

    # zero_count와 same_count를 계산
    for i in lottos:
        if i == 0:
            zero_count += 1
        else:
            if i in win_nums:
                same_count += 1

    # max_count: zero_count를 모두 same으로 바꿔줌
    max_rank = 7 - (same_count + zero_count)

    # min_count: zero_count를 모두 same으로 안바꿈
    min_rank = 7 - same_count

    if max_rank == 7:
        max_rank = 6
    if min_rank == 7:
        min_rank = 6

    # 결과 리턴
    answer = [max_rank, min_rank]
    return answer
