def solution(numbers):
    not_exist = list(set([i for i in range(10)]) - set(numbers))
    answer = sum(not_exist)
    return answer