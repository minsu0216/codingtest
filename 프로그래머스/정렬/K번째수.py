def solution(array, commands):
    answer = [sorted(array[(c[0]-1):(c[1])])[c[2]-1] for c in commands]
    return answer


# 정답
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))