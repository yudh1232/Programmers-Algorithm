from math import gcd

def solution(w,h):
    # 최대공약수만큼 일정 패턴이 반복됨
    g = gcd(w, h)
    
    # 한 패턴내에서 사용할 수 없는 사각형의 수는 (w // g + h // g - 1)
    answer = w * h - g * (w // g + h // g - 1)
    
    # 결과 리턴
    return answer
