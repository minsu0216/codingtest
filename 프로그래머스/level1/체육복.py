def solution(n, lost, reserve):
    answer = 0
    id = [i for i in range(1, n+1)]
    
    for i in range(1, n+1):
        if i not in lost: 
            answer += 1
            id.remove(i)          
        elif i in lost and i in reserve:
            answer += 1
            id.remove(i)
            reserve.remove(i)
    
    for i in id:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    
    return answer