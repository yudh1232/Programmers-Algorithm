def solution(N, number):
    # 다이나믹 프로그래밍, dp[i]: N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]

    # N을 1번~8번 사용
    for i in range(1, 9):
        # 'NNN'형태의 숫자를 추가, 예) i: 3, N: 2일 때 222를 추가
        dp[i].add(int(str(N) * i))
        
        # dp[i]는 dp[j]와 dp[i - j]의 숫자를 조합해서 만들 수 있는 수들의 집합이다
        for j in range(1, i // 2 + 1):
            for a in dp[j]:
                for b in dp[i - j]:
                    # dp[j]와 dp[i - j]의 사칙연산 결과를 dp[i]에 넣음
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(b - a)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
                    if a != 0:
                        dp[i].add(b // a)
        
        # N을 i번 사용해서 number를 만들었다면 
        if number in dp[i]:
            return i
    
    # N을 8번 사용했는데도 number를 못 만들었다면
    return -1
