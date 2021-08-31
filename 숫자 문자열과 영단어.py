def solution(s):
    # "zero"이 있으면 "0"으로 바꿈
    new_s = s.replace("zero", "0")

    # "one"이 있으면 "1"으로 바꿈
    new_s = new_s.replace("one", "1")

    # "two"이 있으면 "2"으로 바꿈
    new_s = new_s.replace("two", "2")

    # "three"이 있으면 "3"으로 바꿈
    new_s = new_s.replace("three", "3")

    # "four"이 있으면 "4"으로 바꿈
    new_s = new_s.replace("four", "4")

    # "five"이 있으면 "5"으로 바꿈
    new_s = new_s.replace("five", "5")

    # "six"이 있으면 "6"으로 바꿈
    new_s = new_s.replace("six", "6")

    # "seven"이 있으면 "7"으로 바꿈
    new_s = new_s.replace("seven", "7")

    # "eight"이 있으면 "8"으로 바꿈
    new_s = new_s.replace("eight", "8")

    # "nine"이 있으면 "9"으로 바꿈
    new_s = new_s.replace("nine", "9")
    
    # 문자열인 new_s를 정수로 바꿔줌
    answer = int(new_s)

    # 결과 리턴
    return answer
