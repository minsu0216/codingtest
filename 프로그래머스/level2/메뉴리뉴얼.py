from itertools import combinations

def solution(orders, course):
    answer = []
    orders.sort(key=len)
    for c in course:
        d = {}
        for order in orders:
            combs = list(map(sorted, list(combinations(order, c))))
            for comb in combs:
                if "".join(comb) in d: continue
                
                n = 0
                for order2 in orders:
                    if all([com in list(order2) for com in comb]): n += 1
                
                if n >= 2: d["".join(comb)] = n
        
        if d: answer.append([dd for dd in d if d[dd] == max(d.values())])
    
    
    answer = sum(answer, [])
    answer.sort()
    
    return answer