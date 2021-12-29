# 내 답
N, K = map(int, input().split())

result = 0
# while True:
#   if N % K == 0:
#     N = N // K
#     result += 1
#     if N == 1: break
#   else:
#     N -= 1
#     result += 1
#     if N == 1: break

# print(result)

# 교재 답
while True:
  target = N // K * K
  result += N - target
  N = target

  if N < K:
    break

  N = N // K
  result += 1

result += N-1
print(result)