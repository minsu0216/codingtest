from itertools import combinations
from math import sqrt

def solution(nums):
    answer = 0
    dummy = list(combinations(nums, 3))
    for d in dummy:
        tmp = sum(d)
        if all([tmp%i!=0 for i in range(2, int(sqrt(tmp))+1)]):
            answer += 1
        
    return answer