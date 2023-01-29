import sys

T = int(sys.stdin.readline())


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


for _ in range(T):
    i, j = map(int, sys.stdin.readline().split())
    print((factorial(j) // factorial(i) // factorial(j - i)))
