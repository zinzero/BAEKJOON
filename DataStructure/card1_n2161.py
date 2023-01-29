import sys

n = int(sys.stdin.readline())

que = []
result = []
for i in range(n):
    que.append(i + 1)

while len(que) > 1:
    result.append(que.pop(0))
    que.append(que.pop(0))

result.append(que.pop())

for i in range(len(result)):
    print(result[i], end=' ')




