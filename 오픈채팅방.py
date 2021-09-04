def solution(record):
    answer = []
    users = {} # 딕셔너리 이용, uid와 nickname을 저장하는 딕셔너리
    print_list = [] # 명령과 uid를 저장하는 리스트 

    # record 리스트의 각 원소에 대하여
    for r in record:
        # 명령이 Enter일 때
        if r[0] == 'E':
            command, uid, nickname = r.split()
            users[uid] = nickname
            print_list.append([command, uid])
        
        # 명령이 Change일 때
        elif r[0] == 'C':
            command, uid, nickname = r.split()
            users[uid] = nickname
        
        # 명령이 Leave일 때
        else:
            command, uid = r.split()
            print_list.append([command, uid])

    for p in print_list:
        # 명령이 Enter일 때
        if p[0] == 'Enter':
            string = users[p[1]] + '님이 들어왔습니다.'
        # 명령이 Leave일 때
        else:
            string = users[p[1]] + '님이 나갔습니다.'              
    
        answer.append(string)

    # 결과 리턴
    return answer
