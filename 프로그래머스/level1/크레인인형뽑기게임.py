def solution(board, moves):
    answer = 0
    
    board = [[b[j] for b in board[::-1] if b[j] != 0] for j in range(len(board))]
    
    bowl = []
    for move in moves:
        if not board[move-1]: continue
            
        bowl.append(board[move-1].pop())
        
        if len(bowl) >= 2:
            if bowl[-1] == bowl[-2]:
                bowl.pop()
                bowl.pop()
                answer += 2
        
    return answer