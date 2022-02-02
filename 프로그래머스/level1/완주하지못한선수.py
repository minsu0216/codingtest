# def solution(participant, completion):
#     answer = ''
#     for p in participant:
#         if p in completion:
#             completion.remove(p)
#         else:
#             answer = p
    
#     # answer = str([p for p in participant if p not in completion])
#     return answer

# def solution(participant, completion):
#     for c in completion:
#         participant.remove(c)
    
#     return participant[0]

def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
    return list(key for key, val in d.items() if val == 1).pop()