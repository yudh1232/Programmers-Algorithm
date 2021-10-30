def solution(str1, str2):
    # 알파벳들을 모두 소문자로 변경
    str1 = str1.lower()
    str2 = str2.lower()

    count = 0  # 총 글자 쌍 수
    str1_dict = {}  # 글자 쌍과 그 글자 쌍의 갯수를 담는 딕셔너리
    str2_dict = {}  # 글자 쌍과 그 글자 쌍의 갯수를 담는 딕셔너리
    
    # str1에서 글자 쌍을 추출하여 str1_dict에 담음
    for i in range(len(str1) - 1):
        # 두 글자가 모두 알파벳일 경우
        if str1[i:i+2].isalpha():
            # 그 글자 쌍이 딕셔너리에 있으면 갯수를 +1 해줌
            if str1[i:i+2] in str1_dict:
                str1_dict[str1[i:i+2]] += 1
            # 그 글자 쌍이 딕셔너리에 없으면 딕셔너리에 추가해줌
            else:
                str1_dict[str1[i:i+2]] = 1
            # 총 글자 쌍수 +1 해줌
            count += 1

    # str2에서 글자 쌍을 추출하여 str2_dict에 담음
    for i in range(len(str2) - 1):
        # 두 글자가 모두 알파벳일 경우
        if str2[i:i+2].isalpha():
            # 그 글자 쌍이 딕셔너리에 있으면 갯수를 +1 해줌
            if str2[i:i+2] in str2_dict:
                str2_dict[str2[i:i+2]] += 1
            # 그 글자 쌍이 딕셔너리에 없으면 딕셔너리에 추가해줌
            else:
                str2_dict[str2[i:i+2]] = 1
            # 총 글자 쌍수 +1 해줌
            count += 1
    
    # 총 글자 쌍이 0개면 유사도는 1이므로 65536 리턴
    if count == 0:
        return 65536
    
    overlapping_count = 0  # 겹치는 쌍의 수
    # str1의 글자 쌍에 대하여
    for key in str1_dict.keys():
        # 글자 쌍이 str2에 있다면
        if key in str2_dict:
            # 겹치는 쌍의 수는 str1과 str2의 있는 개수 중 작은값
            overlapping_count += min(str1_dict[key], str2_dict[key])
    
    # 유사도는 (겹치는 쌍의 수 / 총 글자 쌍 수 - 겹치는 쌍의 수), 결과값 계산
    answer = int(overlapping_count / (count - overlapping_count) * 65536)
    # 결과값 리턴
    return answer
