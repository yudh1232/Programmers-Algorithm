def solution(participant, completion):
    # participant와 completion을 정렬
    participant.sort()
    completion.sort()

    # participant[i]와 completion[i]이 같지않으면 participant[i]를 리턴
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # completion을 다 살펴봤는데 participant와 같았다면 participant에 남은 한명이 정답
    return participant[-1]
