def solution(numbers):
    
    res = []
    first = sorted(set([int(str(n)[0]) for n in numbers]), reverse=True)
    
    for f in first:
        numbers1 = [n for n in numbers if int(str(n)[0]) == f]
        if len(numbers1) > 1:
            res += sorted(numbers1, key=lambda x: int((str(x)*4)[:4]), reverse=True)
            
            # res += sorted(numbers1, key=lambda x: int(str(x)[-1:0]) if (str(x)[-1:0]!='') else int(str(x)[-1]), reverse=True)
            # res += sorted(numbers1, key=lambda x: int(str(x)[-1]), reverse=True)  
        else:
            res += numbers1
    
    if res.count(0) == len(res): answer = "0"
    else: answer = ''.join([str(n) for n in res])
    
    return answer


# 정답
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))