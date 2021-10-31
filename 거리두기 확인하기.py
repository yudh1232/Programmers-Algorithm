from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(places):
    answer = []
    
    # 각 대기실에 대하여
    for place in places:
        # 문자열들을 한 글자씩 잘라서 2차원 리스트로 만듦 
        data = []
        for p in place:
            data.append(list(p))
        
        # 거리두기 체크, 지키고 있으면 answer에 1을 넣고 아니면 0을 넣음
        answer.append(distance_check(data))

    # 결과 리턴
    return answer


# bfs로 거리두기를 체크하는 함수
def distance_check(data):
    q = deque()

    # 각 자리에 대하여
    for x in range(5):
        for y in range(5):
            # 응시자가 있는 자리면
            if data[x][y] == 'P':
                # 응시자로 부터 거리 2까지 bfs
                visited = [[False] * 5 for _ in range(5)]
                visited[x][y] = True
                q.append((x, y, 0))

                while q:
                    # 큐에서 원소를 하나 꺼냄
                    x, y, dist = q.popleft()
                    # 상하좌우에 대하여
                    for d in range(4):
                        # 다음위치 계산
                        nx = x + dx[d]
                        ny = y + dy[d]
                        # 다음위치가 리스트를 벗어나면 통과
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        # 다음위치가 이미 방문한 곳이면 통과
                        if visited[nx][ny]:
                            continue
                        # 응시자를 만났으면 0 리턴(거리두기 안지킴)
                        if data[nx][ny] == 'P':
                            return 0
                        # 빈테이블이면서 거리가 0인 경우
                        elif data[nx][ny] == 'O' and dist == 0:
                            # dist에 +1 해서 큐에 넣음
                            q.append((nx, ny, dist + 1))

    # 1 리턴(거리두기 지킴)
    return 1
