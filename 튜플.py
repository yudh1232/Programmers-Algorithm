def solution(s):
    # 문자열을 '},{'으로 구분하여 분리
    arr = list(s.split('},{'))

    # 분리된 결과 개수가 1개라면, '{{'와 '}}'를 떼어내고 리스트에 넣어서 리턴
    if len(arr) == 1:
        return [int(arr[0][2:-2])]
    # 분리된 결과 개수가 2개 이상이면 
    else:
        # 각 문자열을 정수 리스트로 바꾼것을 넣을 리스트 선언
        arr2 = []
        
        # arr의 맨 앞 원소는 '{{'를 떼고 ','로 구분하여 정수 리스트로 바꿔 넣음
        arr2.append(list(map(int, arr[0][2:].split(','))))
        
        # arr의 맨 뒤 원소는 '}}'를 떼고 ','로 구분하여 정수 리스트로 바꿔 넣음
        arr2.append(list(map(int, arr[len(arr) - 1][:-2].split(','))))
        
        # arr의 맨 앞과 맨 뒤를 제외한 원소들은 ','로 구분하여 정수 리스트로 바꿔 넣음
        for i in range(1, len(arr) - 1):
            arr2.append(list(map(int, arr[i].split(','))))
    
    # arr2의 원소들을 각 원소 리스트의 길이순으로 정렬
    arr2.sort(key = lambda x: len(x))

    # 결과를 담을 리스트
    answer = []

    # arr2의 원소 data 대하여 앞에서부터 탐색
    for data in arr2:
        # data의 원소 d에 대하여
        for d in data:
            # d가 answer에 없다면 
            if d not in answer:
                # answer에 추가하고 break
                answer.append(d)
                break
    
    # 결과 리턴
    return answer
