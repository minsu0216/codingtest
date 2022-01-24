def solution(answers):
    n = len(answers)
    sp1 = [i for _ in range(10000//5) for i in [1,2,3,4,5]][:n]
    sp2 = [i for _ in range(10000//8) for i in [2,1,2,3,2,4,2,5]][:n]
    sp3 = [i for _ in range(10000//10) for i in [3,3,1,1,2,2,4,4,5,5]][:n]
    
    answers = [sum([a == s for a,s in zip(answers, sp1)]),
             sum([a == s for a,s in zip(answers, sp2)]),
             sum([a == s for a,s in zip(answers, sp3)])]
    answer = [i+1 for i, a in enumerate(answers) if a == max(answers)]
    return answer

# def solution(answers):
#     n = len(answers)
#     sp1 = [i for _ in range(10000//5) for i in [1,2,3,4,5]][:n]
#     sp2 = [i for _ in range(10000//8) for i in [2,1,2,3,2,4,2,5]][:n]
#     sp3 = [i for _ in range(10000//10) for i in [3,3,1,1,2,2,4,4,5,5]][:n]
    
#     n_answers = [0, 0, 0]
#     for i, a in enumerate(answers):
#         if sp1[i] == a: n_answers[0] += 1
#         if sp2[i] == a: n_answers[1] += 1
#         if sp3[i] == a: n_answers[2] += 1
    
#     answer = [i+1 for i, a in enumerate(n_answers) if a == max(n_answers)]
#     return answer