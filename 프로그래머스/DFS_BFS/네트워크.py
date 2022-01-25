from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for j, visit in enumerate(visited):
        if not visit:
            queue = deque([j])
            visited[j] = True
            while queue:
                v = queue.popleft()
                for i, c in enumerate(computers[v]):
                    if (not visited[i]) & (c == 1):
                        queue.append(i)
                        visited[i] = True
            answer += 1
    
    return answer