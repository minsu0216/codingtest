import re
def solution(dartResult):
    answer = 0
    d = list(map(int, re.findall('\d+', dartResult)))
    w = re.findall('[SDT]', dartResult)
    staracha = re.findall('[*#]', dartResult)
    
    for i, sdt in enumerate(w):
        if sdt == 'S': d[i] **= 1
        elif sdt == 'D': d[i] **= 2
        else: d[i] **= 3
    
    for i, sa in enumerate(dartResult):
        if sa not in ['*', '#']: continue
        else:
            if i==2: 
                if sa=='*': d[0] = 2 * d[0]
                else: d[0] = -d[0]
            elif i>2 and i<6:
                if sa=='*': 
                    d[0] = 2 * d[0] 
                    d[1] = 2 * d[1]
                else: d[1] = -d[1]
            else:
                if sa=='*': 
                    d[1] = 2 * d[1] 
                    d[2] = 2 * d[2]
                else: d[2] = -d[2]
    
    return sum(d)

# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer