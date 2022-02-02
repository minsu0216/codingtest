def solution(n, arr1, arr2):
    answer = []
    
    def n2(nn):
        res = ''
        while nn:
            res += str(nn % 2)
            nn //= 2
        return ''.join(['0' for _ in range(n-len(res))]) + res[::-1]
    
    for ar1, ar2 in zip(arr1, arr2):
        tmp = ''
        for a1, a2 in zip(n2(ar1), n2(ar2)):
            tmp += ' ' if a1 == '0' and a2 == '0' else '#'
        answer.append(tmp)
    
    return answer