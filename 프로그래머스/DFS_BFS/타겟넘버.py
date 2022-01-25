from itertools import product

def solution(numbers, target):
    calcul_orders = list(product([0,1], repeat=len(numbers)))
    answer = 0    
    for order in calcul_orders:
        res = 0
        for n, c in zip(numbers, order):
            if c == 0: res += n
            else: res -= n
        if res == target: answer += 1
        
    return answer