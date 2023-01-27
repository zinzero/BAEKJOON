import sys

N = int(sys.stdin.readline().strip())

arr = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), name))

# 버블정렬 하면 시간초과 뜸 ㅠㅠ
# for i in range(len(arr), 1, -1):
#     for j in range(i - 1):
#         if int(arr[j][0]) > int(arr[j + 1][0]):
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr.sort(key=lambda x: x[0])    # lambda 를 이용해서 나이순 정렬
for i in arr:
    print(i[0], i[1])
