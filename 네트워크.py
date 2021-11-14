# dfs 방식으로 노드들을 순회
def dfs(now, n, computers, visited):
    # 방문 표시
    visited[now] = True

    for i in range(n):
        # 현재 노드와 연결된 곳 중에서 아직 방문하지 않았다면
        if computers[now][i] == 1 and not visited[i]:
            # dfs 수행
            dfs(i, n, computers, visited)


def solution(n, computers):
    answer = 0

    # dfs를 위한 visited 리스트 생성
    visited = [False] * n

    # 각 노드에 대하여
    for i in range(n):
        # 아직 방문하지 않았으면
        if not visited[i]:
            # dfs 수행
            dfs(i, n, computers, visited)
            
            # 네트워크 수 1 증가
            answer += 1

    # 결과 리턴
    return answer
