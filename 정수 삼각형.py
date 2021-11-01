def solution(triangle):
    # 삼각형의 높이
    h = len(triangle)

    # dp 리스트 생성
    dp = [[0] * h for _ in range(h)]
    # dp 초기값 설정
    dp[0][0] = triangle[0][0]

    # dp[i][j]는 dp[i - 1][j - 1], dp[i - 1][j] 중 큰 값에 triangle[i][j]를 더한 값임
    for i in range(1, h):
        for j in range(i + 1):
            # 왼쪽 위가 삼각형을 벗어나면
            if j == 0:
                left = 0  # 왼쪽 위를 0으로 설정
            # 왼쪽 위가 삼각형을 벗어나지 않으면
            else:
                left = dp[i - 1][j - 1]  # 왼쪽 위 값을 구함
            
            # 오른쪽 위가 삼각형을 벗어나면
            if j == i:
                right = 0  # 오른쪽 위를 0으로 설정
            # 오른쪽 위가 삼각형을 벗어나지 않으면
            else:
                right = dp[i - 1][j]  # 오른쪽 위 값을 구함

            # dp[i][j]를 구함
            dp[i][j] = max(left, right) + triangle[i][j]
    
    # 경로의 합 중 가장 큰 값 리턴
    return max(dp[h - 1])
