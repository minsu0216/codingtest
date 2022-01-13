# 내 답
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
  A.sort()
  B.sort(reverse=True)
  A[0], B[0] = B[0], A[0]

print(sum(A))



# 교재 답
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
  # A의 원소가 B의 원소보다 작은 경우
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))