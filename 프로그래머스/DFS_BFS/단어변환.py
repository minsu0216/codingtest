from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    else:
        n = len(begin)
        visited = [False] * len(words)
        queue = deque([(begin, 0)])
        while all([target != i[0] for i in queue]):
            current = queue.popleft()
            candidates = [w for w in words if sum([i==j for i, j in zip(current[0], w)]) == n-1]
            for s in candidates:
                if not visited[words.index(s)]:
                    queue.append((s, current[1]+1))
                    visited[words.index(s)] = True
        for w, a in queue:
            if w == target: answer = a
    return answer