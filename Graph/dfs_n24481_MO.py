import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]
depth = [-1] * (N + 1)
count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    global count
    depth[V] = count
    for g in range(1, N + 1):
        if depth[g] == -1 and matrix[V][g] == 1:
            count += 1
            dfs(g)

dfs(R)

for i in range(1, N + 1):
    print(depth[i])

# 메모리 초과...