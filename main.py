from collections import deque
a = deque([('adsf', 1)])
b = a.popleft()
a.append(('sdf', 2))
print(a)