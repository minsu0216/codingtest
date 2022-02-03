def solution(n):
    answer = 0
    
    for i in range(1, int(n/2)+1):
        res = 0
        for j in range(i, n+1):
            res += j
            if res == n:
                answer += 1
                break
            elif res > n:
                break
    
    return answer+1