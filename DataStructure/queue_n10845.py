import sys

n = int(sys.stdin.readline())

que = []

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        que.append(order[1])
    elif order[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif order[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

