import sys

N = int(sys.stdin.readline().strip())

arr = []

for _ in range(N):
    line = sys.stdin.readline().strip()
    # arr.append(line.split())
    arr.append(line)

arr.sort()

for i in arr:
    print(i)


