# def solution(a, b):
#     answer = 0
#     for i in range(min(a,b), max(a,b)+1): answer += i 
#     return answer

def solution(a, b):
    return sum(range(min(a,b), max(a,b) + 1))