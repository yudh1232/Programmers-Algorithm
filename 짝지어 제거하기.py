def solution(s):
    # 스택 생성
    stack = []

    # 문자열 s의 각 문자를 살펴봄
    for i in range(len(s)):
        c = s[i]

        # 스택이 비어있다면
        if len(stack) == 0:
            # c를 넣음
            stack.append(c)
        # 스택이 비어있지않다면
        else:
            # top과 c가 같으면 팝
            if stack[-1] == c:
                stack.pop()
            # top과 c가 다르면 c를 넣음
            else:
                stack.append(c)
    
    # 문자열 s를 다 살펴본뒤 stack에 남아있는게 없다면 짝지어 제거하기 성공
    if len(stack) == 0:
        return 1
    # 남아있는게 있다면 짝지어 제거하기 실패
    else:
        return 0
