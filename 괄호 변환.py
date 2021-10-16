# 재귀적으로 올바른 괄호 문자열을 구하는 함수
def convert(p):
    # 빈 문자열일 경우 빈 문자열 반환
    if len(p) == 0:
        return ''
    
    proper_flag = True # 올바른 괄호 문자열인지 나타내는 플래그
    open_count = 0 # '('의 개수
    close_count = 0 # ')'의 개수

    for i in range(len(p)):
        # '(', ')'의 개수를 셈
        if p[i] == '(':
            open_count += 1
        else:
            close_count += 1

        # ')'가 많으면 올바른 괄호 문자열이 아님    
        if open_count < close_count:
            proper_flag = False
        # 균형잡힌 괄호 문자열이면
        if open_count == close_count:
            # u, v 분리
            u = p[:i+1]
            v = p[i+1:]
            
            # 올바른 괄호 문자열이면 u + convert(v) 리턴
            if proper_flag == True:
                return u + convert(v)
            # 올바른 괄호 문자열이 아니면
            else:
                # '(' + convert(v) + ')' + u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집은 결과를 리턴
                s = '(' + convert(v) + ')'
                temp = ''
                for i in range(1, len(u) - 1):
                    if u[i] == '(':
                        temp += ')'
                    else:
                        temp += '('
                return s + temp


def solution(p):
    # 재귀로 answer를 구함
    answer = convert(p)
    return answer
