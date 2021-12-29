n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# result = 0
data.sort(reverse=True)
# for i in range(m):
#   if i % (k+1) == k:
#     result += data[1]
#   else:
#     result += data[0]

# print(result)

result = (m // (k+1)) * (data[0]*k + data[1]) + (m % (k+1))*data[0]
print(result)