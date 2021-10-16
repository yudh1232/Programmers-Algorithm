from itertools import combinations

def solution(orders, course):
    answer = []

    # orders의 각 문자열을 문자배열로바꾸고 정렬한 결과를 담는 리스트
    new_orders = []
    for order in orders:
        order = list(order)
        order.sort()
        new_orders.append(order)

    # 각 메뉴 가지수 c에 대하여
    for c in course:
        dic = {}
        dic_max = 0
        # 각 주문에 대하여
        for no in new_orders:
            # c개를 뽑는 조합에 대하여 등장횟수를 셈
            for combi in combinations(no, c):
                if combi in dic:
                    dic[combi] += 1
                else:
                    dic[combi] = 1

        # 최고등장횟수를 구함
        if dic:
            dic_max = max(dic.values())
        
        # 최고등장횟수에 해당하는 조합을 answer에 문자열로 넣음
        if dic_max >= 2:
            for d in dic:
                if dic[d] == dic_max:
                    answer.append(''.join(d))
    
    # answer를 정렬
    answer.sort()

    # 결과 리턴
    return answer
