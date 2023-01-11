import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[0] for _ in range(N+1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    global count
    visited[V] = count
    graph[V].sort()
    graph[V].reverse()
    for g in graph[V]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
