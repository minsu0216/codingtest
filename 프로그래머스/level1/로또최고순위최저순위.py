def solution(lottos, win_nums):
    answer = [0] * 2
    
    n_0 = sum([True for i in lottos if i == 0])
    correct = len(set(lottos) & set(win_nums))
    
    answer[0] = correct + n_0
    answer[1] = correct
    
    for i in range(2):
        answer[i] = abs(answer[i] - 7)
        if answer[i] >= 6: answer[i] = 6

        
    return answer