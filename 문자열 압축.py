def solution(s):
    unit = 1 # 자르는 단위
    length = len(s) # 원래 문자열의 길이
    result = length # 결과값 초기화

    # 자르는 단위를 1부터 1씩증가시키며 압축해봄
    while True:
        # 자르는 단위가 원래 문자열 길이의 절반보다 크면 반복 종료
        if unit > length // 2:
            break

        new_s = '' # 압축된 문자열
        count = 1 # 단위의 반복횟수

        for i in range(unit, length + unit, unit):
            # 이전단위와 현재단위가 같다면
            if s[i-unit:i] == s[i:i+unit]:
                # 단위 반복횟수 증가
                count += 1
            # 이전단위와 현재단위가 다르다면, 압축문자열에 반복횟수와 이전단위를 넣어줌
            else:
                if count == 1:
                    new_s += s[i-unit:i]
                else:
                    new_s += str(count) + s[i-unit:i]
                # 반복횟수를 1로 재설정
                count = 1

        result = min(result, len(new_s)) # 결과값 계산
        unit += 1 # 자르는 단위 증가  
        
    return result
