def solution(n):
    string = ''
    
    # n이 0이 될 때까지 3으로 나눔
    while n > 0:
        # n이 3으로 나누어 떨어지면 몫에서 1을 빼고 문자열에 '4' 추가
        if n % 3 == 0:
            string += '4'
            n = n // 3 - 1
        # 나머지가 1이면 문자열에 '1' 추가
        elif n % 3 == 1:
            string += '1'
            n = n // 3
        # 나머지가 2이면 문자열에 '2' 추가
        elif n % 3 == 2:
            string += '2'
            n = n // 3

    # 문자열을 뒤집음
    answer = string[::-1]

    # 결과 리턴
    return answer
