# def solution(n):
#     answer = n-1
#     for i in range(2, n+1):
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 answer -= 1
#                 break    
#     return answer

def solution(n):
    tf = [True] * (n+1)
    for i in range(2, n+1):
        if tf[i]:
            for j in range(i*2, n+1, i):
                tf[j] = False
    x = [i for i in range(2, n+1) if tf[i]]
    answer = len(x)
    return answer