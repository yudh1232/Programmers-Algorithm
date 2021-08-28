def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp = new_id
    new_id = ''.join(c for c in temp if c.isalnum() or c == '-' or c == '_' or c == '.')

    # 3단계
    temp = new_id # temp에 new_id 복사
    new_id = '' # 3단계의 결과 문자열

    # temp 문자열의 각 문자에 대하여
    for i in range(len(temp)):
        # 마침표가 아니면 new_id에 추가
        if temp[i] != '.':
            new_id += temp[i]
        # 마침표이지만 첫글자이면 new_id에 추가
        elif i == 0:
            new_id += temp[i]
        # 마침표이면서 앞에글자가 마침표가 아니면 new_id에 추가
        elif temp[i] != temp[i - 1]:
            new_id += temp[i]

    # 4단계
    # 첫 글자가 마침표이면 제거
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    # 끝 글자가 마침표이면 제거
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[0:-1]

    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[0:-1]

    # 7단계
    if len(new_id) <= 2:
        # c에 마지막 문자를 담고 길이가 3이 될 때까지 끝에 붙임
        c = new_id[-1]
        while len(new_id) <= 2:
            new_id += c

    answer = new_id
    return answer
