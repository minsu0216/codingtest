from collections import deque
def solution(rows, columns, queries):
    answer = []
    
    mat = [i for i in range(1, rows*columns+1)]
    
    for q in queries:
        
        # 회전 대상 id 
        id = []
        i = q[0]
        j = q[1]
        
        while j != q[3]:
            j += 1
            id.append(columns*(i-1)+j)
        while i != q[2]:
            i += 1
            id.append(columns*(i-1)+j)
        while j != q[1]:
            j -= 1
            id.append(columns*(i-1)+j)
        while i != q[0]:
            i -= 1
            id.append(columns*(i-1)+j)
        
        # 최소값 계산
        answer.append(min([mat[i-1] for i in id]))
        
        # 회전
        before = deque([])
        before.append(mat[id[-1]-1])
        for i in range(len(id)):
            before.append(mat[id[i]-1])
            mat[id[i]-1] = before.popleft()
            
    
    return answer