import sys

N, K = map(int, sys.stdin.readline().split())

que = []
for i in range(N):
    que.append(i + 1)


result = []
while que:
    for idx in range(K - 1):
        que.append(que.pop(0))
    result.append(que.pop(0))

answer = ", ".join(map(str, result))
print('<' + answer + '>')
