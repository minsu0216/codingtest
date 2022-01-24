def solution(brown, yellow):
    n = brown + yellow
    candidate = [(n//i, i) for i in range(1, int(n**(0.5))+1) if (n%i == 0) & (i >= 3)]
    for c in candidate:
        if (c[0]-2)*(c[1]-2) == yellow: answer = c
    # answer = [c for c in candidate if (c[1]-2)*(c[0]-2) == yellow]
    return answer