N = int(input())
directions = list(input().split())

pos = [1, 1]

for d in directions:
  if (d == 'L') & (pos[1]-1 != 0):
    pos[1] -= 1
  elif (d == 'R') & (pos[1]+1 != N+1):
    pos[1] += 1
  elif (d == 'U') & (pos[0]-1 != 0):
    pos[0] -= 1
  elif (d == 'D') & (pos[0]+1 != N+1):
    pos[0] += 1

print(pos[0], pos[1])

############################################

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > x or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x, y)