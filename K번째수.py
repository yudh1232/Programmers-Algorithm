def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        
        # array에서 i번째부터 j번째까지 자르고 정렬
        arr = array[i-1:j]
        arr.sort()

        # arr의 k번째 숫자를 answer에 넣음
        answer.append(arr[k - 1])

    # 결과 리턴
    return answer
