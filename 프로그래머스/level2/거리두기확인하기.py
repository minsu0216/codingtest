def solution(places):
    answer = [1, 1, 1, 1, 1]
    
    def mdistance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    for p_i, place in enumerate(places):
        xy = [(i,j) for i in range(5) for j in range(5) if place[i][j] == "P"]
        
        if len(xy) <= 1: continue
        
        for p1 in range(len(xy)):
            for p2 in range(p1+1, len(xy)):
                
                if mdistance(xy[p1], xy[p2]) > 2: continue
                elif mdistance(xy[p1], xy[p2]) == 1: 
                    answer[p_i] = 0
                    break
                else:
                    min_x = min(xy[p1][0], xy[p2][0])
                    max_x = max(xy[p1][0], xy[p2][0])
                    min_y = min(xy[p1][1], xy[p2][1])
                    max_y = max(xy[p1][1], xy[p2][1])
                    if any([place[i][j]!="X" for i in range(min_x, max_x+1) for j in range(min_y, max_y+1) if place[i][j] != "P"]):
                        answer[p_i] = 0
                        break
                        
            if answer[p_i] == 0: break
    
    return answer