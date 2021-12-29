'''
deque
연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때 매우 효과적
시간 복잡도 O(1) / 리스트는 O(N)
인덱싱, 슬라이싱 등의 기능은 사용할 수 없음
스택이나 큐의 기능을 모두 포함
popleft() / pop()
appendleft(x) / append(x)
'''
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

'''
Counter
등장 횟수를 세는 기능 제공
'''
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))