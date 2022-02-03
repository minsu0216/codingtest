# import re
# def solution(record):
#     answer = []
#     uids = []
#     inp = ['Enter', 'Leave', 'Change']
#     outp = ['님이 들어왔습니다.', '님이 나갔습니다.']
#     for rc in record:
#         tmp = rc.split(" ")
        
#         if tmp[0] == inp[0]:
#             if tmp[1] in uids:
#                 for i in range(len(answer)):
#                     if uids[i] == tmp[1]:
#                         inorout = "".join(re.findall('[(님이 들어왔습니다.)(님이 나갔습니다.)]', answer[i]))
#                         answer[i] = tmp[2] + inorout
#             answer.append(tmp[2] + outp[0])
#             uids.append(tmp[1])
            
#         elif tmp[0] == inp[1]:
#             for id, a in zip(uids[::-1], answer[::-1]):
#                 if tmp[1] == id:
#                     name = "".join(re.findall('[(a-zA-Z)]', a))
#                     answer.append(name + outp[1])
#                     uids.append(tmp[1])
#                     break
                    
#         else:
#             for i in range(len(answer)):
#                 if uids[i] == tmp[1]:
#                     inorout = "".join(re.findall('[(님이 들어왔습니다.)(님이 나갔습니다.)]', answer[i]))
#                     answer[i] = tmp[2] + inorout
                    
#     return answer

def solution(record):
    answer = []
    user = {}
    for a in record:
        command = a.split()
        if command[0] == 'Enter' or command[0] == 'Change':
            user[command[1]] = command[2]
    for a in record:
        command = a.split()
        if command[0] == 'Enter':
            answer.append(f'{user[command[1]]}님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(f'{user[command[1]]}님이 나갔습니다.')

    return answer