from itertools import permutations

def solution(expression):
    answer = 0

    # expression에서 연산자의 인덱스를 리스트에 넣음
    operation_index = []
    for i in range(len(expression)):
        if not expression[i].isdigit():
            operation_index.append(i)
    
    # (1, 2, 3)으로 만든 순열에 대하여
    for p in permutations((1, 2, 3), 3):
        # a는 '+', b는 '-', c는 '*', 숫자가 클수록 우선순위가 높음
        a, b, c = p

        prefix = [] # prefix 형태의 수식을 담는 리스트
        stack = [] # 연산자들을 담는 스택
        i = 0 # expression 순회에 쓰일 인덱스
        
        # infix 형태의 수식을 prefix로 바꿔 prefix 리스트에 넣음
        for o in operation_index:
            # 숫자부분을 prefix에 넣음
            prefix.append(int(expression[i:o]))

            # 연산자 처리
            if len(stack) == 0:
                stack.append(expression[o])
            else:
                if expression[o] == '+':
                    while len(stack) > 0:
                        if stack[-1] == '+':
                            prefix.append(stack.pop())
                        elif stack[-1] == '-':
                            if a > b:
                                break
                            else:
                                prefix.append(stack.pop())
                        else:
                            if a > c:
                                break
                            else:
                                prefix.append(stack.pop())
                    stack.append('+')
                elif expression[o] == '-':
                    while len(stack) > 0:
                        if stack[-1] == '-':
                            prefix.append(stack.pop())
                        elif stack[-1] == '+':
                            if b > a:
                                break
                            else:
                                prefix.append(stack.pop())
                        else:
                            if b > c:
                                break
                            else:
                                prefix.append(stack.pop())
                    stack.append('-')
                else:
                    while len(stack) > 0:
                        if stack[-1] == '*':
                            prefix.append(stack.pop())
                        elif stack[-1] == '+':
                            if c > a:
                                break
                            else:
                                prefix.append(stack.pop())
                        else:
                            if c > b:
                                break
                            else:
                                prefix.append(stack.pop())
                    stack.append('*')

            i = o + 1

        # 마지막 연산자 뒤의 숫자 처리
        prefix.append(int(expression[operation_index[-1]+1:]))
        
        # 스택에 남아있는 연산자 처리
        while len(stack) > 0:
            prefix.append(stack.pop())

        # 이번 순열의 값 계산
        current = 0
        for pre in prefix:
            if pre == '+':
                oper2 = stack.pop()
                oper1 = stack.pop()
                stack.append(oper1 + oper2)
            elif pre == '-':
                oper2 = stack.pop()
                oper1 = stack.pop()
                stack.append(oper1 - oper2)
            elif pre == '*':
                oper2 = stack.pop()
                oper1 = stack.pop()
                stack.append(oper1 * oper2)
            else:
                stack.append(pre)
        
        # 이번 순열의 값
        current = abs(stack.pop())

        # 최대값으로 업데이트
        answer = max(answer, current)
    
    # 결과 리턴
    return answer
