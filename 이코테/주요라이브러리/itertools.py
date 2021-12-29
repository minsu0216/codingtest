'''
itertools
반복되는 데이터를 처리하는 기능
순열, 조합, 중복 순열, 중복 조합
'''

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result1 = list(permutations(data, 2))
result2 = list(combinations(data, 2))
result3 = list(product(data, repeat=2))
result4 = list(combinations_with_replacement(data, 2))

print(result1)
print(result2)
print(result3)
print(result4)