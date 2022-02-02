def solution(n):
    answer = 0
    
    rn3 = ''
    while n > 0:
        rn3 += str(n % 3)
        n //= 3
    
    answer = sum([(3**i)*int(n) for i, n in enumerate(rn3[::-1])])
    
    return answer