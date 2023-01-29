N = int(input())

arr = []

def recur(n):
    if n == 1:
        arr.append(1)
    elif n // 2 == 1:
        arr.append(n % 2)
        arr.append(1)
    else:
        arr.append(n % 2)
        recur(n // 2)

recur(N)

for _ in range(len(arr)):
    print(arr.pop(), end='')
