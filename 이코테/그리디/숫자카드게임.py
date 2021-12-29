# 내 답
N, M = map(int, input().split())
data = []
for i in range(N):
  data.append(min(list(map(int, input().split()))))

print(max(data))

# 교재 답
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split())
  min_value = min(data)
  result = max(result, min_value)

print(result)