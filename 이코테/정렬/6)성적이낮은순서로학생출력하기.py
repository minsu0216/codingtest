# # 내 답
N = int(input())
stud_info = [list(input().split()) for i in range(N)]
for i in range(len(stud_info)):
  stud_info[i][1] = int(stud_info[i][1])

stud_info.sort(key=lambda x: x[1])
for i in stud_info:
  print(i[0], end=" ")



# 교재 답
# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
  print(student[0], end=' ')
