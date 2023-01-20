import sys
sys.setrecursionlimit(10**9)    # 재귀 최대 깊이 증가

N, M, R = map(int, sys.stdin.readline().split())    # 정점, 간선, 시작정점

graph = [[] for _ in range(N + 1)]      # [[], [], [], ... , []]
visited = [0] * (N + 1)     # [0, 0, 0, 0, ... , 0]
count = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    global count
    visited[V] = count
    graph[V].sort()
    for g in graph[V]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
