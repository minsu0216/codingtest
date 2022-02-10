# import re
# from itertools import permutations
# def solution(expression):
#     answer = 0
    
#     comps = re.findall('[*+-]', expression)
    
#     perms = list(permutations(set(comps), len(set(comps))))
    
#     for perm in perms:
#         e_copy = expression
#         digits = re.sub('[*+-]', ' ', expression).split(' ')
#         for p in perm:
#             while p in e_copy:
#                 i = e_copy.index(p)
#                 left_i = i-len(digits[2*i]) 
#                 right_i = i+len(digits[2*i+2])
#                 e_copy = e_copy[:left_i] + str(eval(e_copy[left_i:(right_i+1)])) + e_copy[(right_i+1):]
#                 digits = re.sub('[*+-]', ' ', e_copy).split(' ')
#         if abs(int(e_copy)) > answer: answer = abs(int(e_copy))
        
    
#     return expression[1234:]

from itertools import permutations
def solution(expression):
    symbol = ['+', '-', '*']
    answer = []
    for per in permutations(symbol):
        f, s = per[0], per[1]
        lst = []
        for e in expression.split(f):
            temp = [f"({i})" for i in e.split(s)]
            lst.append(f'({s.join(temp)})')
        answer.append(abs(eval(f.join(lst))))
    return max(answer)