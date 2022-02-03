def solution(s):
    answer = -1
    
#     n = len(s)+1
#     start = 0
#     while n > len(s):
        
#         if s == '': return 1
        
#         n = len(s)
#         for i in range(start, len(s)-1):
#             if s[i] == s[i+1]:
#                 s = s[:i] + s[(i+2):]
#                 start = 0 if i == 0 else i-1
#                 break
#     return -1
    s = list(s)
    res = []
    for ss in s:
        res.append(ss)
        if len(res) < 2: continue
        if res[-1] == res[-2]:
            res.pop()
            res.pop()
    if not res: return 1
    else: return 0