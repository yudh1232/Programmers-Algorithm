from collections import deque

def solution(board, moves):
    # 정사각 격자의 크기
    n = len(board)

    # 열 별로 큐를 만들어서 관리
    q_list = [deque() for i in range(n)]

    # board를 위에서부터 살피며 열 별로 큐를 채움
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                q_list[j].append(board[i][j])

    # basket은 스택으로 관리
    basket = []

    # 결과값
    answer = 0


    for m in moves:
        # 큐가 비어있으면 continue
        if len(q_list[m - 1]) == 0:
            continue
        # 아니면 인형을 빼냄    
        else:
            item = q_list[m - 1].popleft()
        
        # basket이 비어있으면 인형을 넣음
        if len(basket) == 0:
            basket.append(item)
        # 비어있지 않으면
        else:
            top = basket[-1]
            
            # top과 인형을 교해서 같으면
            if top == item:
                basket.pop()
                answer += 2
            # 다르면
            else:
                basket.append(item)

    # 결과 리턴
    return answer
