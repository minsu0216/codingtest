from itertools import permutations
from math import sqrt, floor

def solution(numbers):
    
    answer = 0    
    candidate = set([int("".join(ns)) for i in range(1, len(numbers)+1) for ns in list(permutations([n for n in numbers], i))])
    # candidate = []
    # for i in range(1, len(numbers)+1):
    #     for number in list(permutations([n for n in numbers], i)):
    #         candidate.append(int("".join(number)))
    # candidate = set(candidate)
    # for c in candidate:
    #     if all([c%j != 0 for j in range(2, floor(sqrt(c)) + 1)]) & (c > 1):
    #         answer += 1
    answer = sum([1 if all([c%j != 0 for j in range(2, floor(sqrt(c)) + 1)]) & (c > 1) else 0 for c in candidate])
            
    return answer