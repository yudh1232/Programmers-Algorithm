def solution(numbers, hand):
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, #의 좌표
    coor = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]

    # 왼손이 *, 오른손이 #에 있는 상태
    hand_pos = [10, 11]

    answer = ''

    for n in numbers:
        # n이 1, 4, 7이면 왼손으로 누름
        if n == 1 or n == 4 or n == 7:
            hand_pos[0] = n
            answer += 'L'
        
        # n이 3, 6, 9이면 오른손으로 누름
        elif n == 3 or n == 6 or n == 9:
            hand_pos[1] = n
            answer += 'R'

        # n이 2, 5, 8, 0이면
        else:
            # 왼손과의 거리와 오른손과의 거리를 구함
            left_dist = abs(coor[hand_pos[0]][0] - coor[n][0]) + abs(coor[hand_pos[0]][1] - coor[n][1])
            right_dist = abs(coor[hand_pos[1]][0] - coor[n][0]) + abs(coor[hand_pos[1]][1] - coor[n][1])

            # 오른손이 더 가깝다면
            if left_dist > right_dist:
                hand_pos[1] = n
                answer += 'R'
            # 왼손이 더 가깝다면
            elif left_dist < right_dist:
                hand_pos[0] = n
                answer += 'L'
            # 거리가 같다면
            else:
                # 왼손잡이라면
                if hand == 'left':
                    hand_pos[0] = n
                    answer += 'L'
                # 오른손 잡이라면
                else:
                    hand_pos[1] = n
                    answer += 'R'

    return answer
