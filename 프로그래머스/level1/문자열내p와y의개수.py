# def solution(s):
#     answer = True
#     s = s.lower()
#     if 'p' not in s and 'y' not in s: return True
#     else: return sum(['p' == i for i in s]) == sum(['y' == i for i in s])

def solution(s):
    s = s.lower()
    if 'p' not in s and 'y' not in s: return True
    else: return s.count('p') == s.count('y')
