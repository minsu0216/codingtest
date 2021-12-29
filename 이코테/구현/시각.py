N = int(input())

res = 0
for h in range(N+1):
  if '3' in str(h): 
    res += 60 * 60
    continue
  
  for m in range(60):
    if '3' in str(m):
      res += 60
      continue
     
    for s in range(60):
      if '3' in str(s):
        res += 1

print(res)

############################################

# H를 입력받기
h = int(input())

count =0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)