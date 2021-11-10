def solution(arr1, arr2):
    # arr1[i][j]에 arr2[i][j]를 더함
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]

    # 결과 리턴
    return arr1
