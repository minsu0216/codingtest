def solution(p):
    
    # 1
    if p == "": return p
    
    # 2
    i = 2
    while True:
        if sum([1 if s == "(" else 0 for s in p[:i]]) == i//2:
                u = p[:i]
                v = p[i:]
                break
        else:
            i += 2

    # 3 
    if u[0] == "(": 
        return u + solution(v)
    # 4
    else:
        return "(" + solution(v) + ")" + "".join([")" if u[1:-1][i] == "(" else "(" for i in range(len(u)-2)])