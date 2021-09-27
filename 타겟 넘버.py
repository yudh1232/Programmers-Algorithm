# 결과값을 전역변수로 선언
answer = 0

# dfs방식으로 numbers[count]를 더하거나 빼서 타겟 넘버를 만듦
def dfs(now, count, numbers, length, target):
    global answer
    # numbers의 모든 원소를 살펴봤으면
    if count == length:
        # 만든 숫자가 타겟과 같다면
        if now == target:
            answer += 1 # answer 1증가
        return
    
    # numbers[count]를 더함
    dfs(now + numbers[count], count + 1, numbers, length, target)
    # numbers[count]를 뺌
    dfs(now - numbers[count], count + 1, numbers, length, target)
    

def solution(numbers, target):
    global answer
    # dfs
    dfs(0, 0, numbers, len(numbers), target)

    # 결과 리턴
    return answer
