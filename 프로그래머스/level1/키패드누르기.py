def solution(numbers, hand):
    answer = ''    
    d = {'0':[0,0], '*':[-1,0], '#':[1,0],
        '7':[-1,1], '8':[0,1], '9':[1,1],
        '4':[-1,2], '5':[0,2], '6':[1,2],
        '1':[-1,3], '2':[0,3], '3':[1,3]}
    pos = [d['*'], d['#']]
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            pos[0] = d[str(n)]
        elif n in [3,6,9]:
            answer += 'R'
            pos[1] = d[str(n)]
        else:
            l_dist = abs(pos[0][0] - d[str(n)][0]) + abs(pos[0][1] - d[str(n)][1])
            r_dist = abs(pos[1][0] - d[str(n)][0]) + abs(pos[1][1] - d[str(n)][1])
            if l_dist > r_dist:
                answer += 'R'
                pos[1] = d[str(n)]
            elif l_dist < r_dist:
                answer += 'L'
                pos[0] = d[str(n)]
            else:
                answer += hand[0].upper()
                if hand == 'right': pos[1] = d[str(n)]
                else: pos[0] = d[str(n)]
        
    return answer