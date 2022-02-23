from collections import Counter

def solution(s):
    answer = []
    nums = list(map(lambda x: x.replace("{", "").replace("}", ""), list(s.split(","))))
    nums_counts = Counter(nums)
    answer = [int(num) for num in nums_counts.keys()]
    answer.sort(key=lambda x: nums_counts.get(str(x)), reverse=True)
    return answer