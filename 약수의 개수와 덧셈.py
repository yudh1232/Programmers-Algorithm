def solution(left, right):
    answer = 0

    # left~right의 수를 살펴봄, i가 제곱수이면 약수의개수는 홀수다
    for i in range(left, right + 1):        
        # i가 제곱수이면
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        # i가 제곱수가 아니면
        else:
            answer += i
    
    # 결과 리턴
    return answer
