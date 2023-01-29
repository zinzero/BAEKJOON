import sys

num = list(map(int, sys.stdin.readline().split()))
num.sort()

if num[2] == num[1] == num[0]:
    print(10000 + num[2] * 1000)
elif num[2] != num[1] == num[0]:
    print(1000 + num[1] * 100)
elif num[2] == num[1] != num[0]:
    print(1000 + num[1] * 100)
else:
    print(num[2] * 100)
