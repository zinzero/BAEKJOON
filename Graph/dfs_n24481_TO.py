import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [-1 for _ in range(N + 1)]

def dfs(V, depth):
    visited[V] = depth

    for i in graph[V]:
        if visited[i] == -1:
            dfs(i, depth + 1)
    return

for j in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in graph:
    k.sort()

dfs(R, 0)

for i in range(1, N + 1):
    print(visited[i])

# 시간 초과
