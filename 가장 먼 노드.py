from collections import deque

def solution(n, edge):
    # graph와 visited 리스트 생성
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    # 그래프 정보를 입력받음
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    # bfs를 위한 큐 생성
    q = deque()

    # 시작노드는 1
    start = 1
    q.append(start)
    visited[start] = True 

    # bfs
    while q:
        # 레벨별로 큐를 돌리기 위한 size 변수 
        size = len(q)

        for _ in range(size):
            # 큐에서 노드를 하나 꺼냄
            now = q.popleft()
            # now에서 갈 수 있는 노드중에서
            for next in graph[now]:
                # 아직 방문하지 않았다면
                if not visited[next]:
                    # 큐에 넣음 방문처리
                    q.append(next)
                    visited[next] = True

    # 마지막 레벨의 size가 결과, 결과 리턴
    return size
