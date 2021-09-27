from itertools import combinations

# num 소수인지 판별하는 함수
def is_prime(num):
    # 2부터 num의 제곱근까지만 살펴보면 됨
    for i in range(2, int(num ** 0.5) + 1):
        # 1이외의 숫자로 나누어떨어지면 소수가아님
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    # nums에서 숫자 3개를 뽑는 조합
    for combi in combinations(nums, 3):
        # 뽑은 숫자 3개를 더한 값이 소수가 맞다면
        if is_prime(sum(combi)):
            answer += 1

    # 결과 리턴
    return answer
