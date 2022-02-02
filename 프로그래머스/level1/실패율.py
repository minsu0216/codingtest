from collections import Counter
def solution(N, stages):
    answer = []
    fail = []
    n = len(stages)
    d = dict(Counter(stages))
    for i in range(1, N+1):
        a = sum([d[s] if s > i else 0 for s in d])
        b = sum([d[s] if s >= i else 0 for s in d])
        if b != 0: 
            fail.append([i, 1 - a/b])
        else: fail.append([i, 0])
        
    answer = [i for i, _ in sorted(fail, key=lambda x: x[1], reverse=True)]
    return answer