import sys

n, m = map(int, sys.stdin.readline().split())

number = list(map(int, sys.stdin.readline().split()))

# result = 0
# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     for idx in range(i - 1, j):
#         result += number[idx]
#
#     print(result)
#     result = 0

temp = 0
pre_sum = [0]
for i in number:
    temp += i
    pre_sum.append(temp)

for idx in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(pre_sum[j] - pre_sum[i - 1])
