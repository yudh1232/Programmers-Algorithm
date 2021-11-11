def solution(phone_number):
    # 뒤에 4자리를 제외한 나머지 숫자의 갯수만큼 *을 표시하고. 뒤 4자리 숫자를 이어붙임
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    
    # 결과 리턴
    return answer
