from collections import deque
def solution(progresses, speeds):
    answer = []
    
    q_pg = deque(progresses)
    q_sp = deque(speeds)

    while q_pg:
        for i in range(len(q_pg)):
            q_pg[i] += q_sp[i]
        n = 0
        while q_pg[0] >= 100:
            q_pg.popleft()
            q_sp.popleft()
            n += 1
            if not q_pg: break
            
        if n > 0: answer.append(n)

    return answer