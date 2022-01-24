def solution(citations):
    n = len(citations)
    answer = 0
    for h in range(n):
        if (sum([i >= h for i in citations]) >= h) & (sum([i < h for i in citations]) < h):
            answer = h
    return answer
    