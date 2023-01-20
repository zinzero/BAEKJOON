import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().strip())   # 정점
M = int(sys.stdin.readline().strip())   # 간선 

graph = [[] for _ in range(N + 1)]
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

    for g in graph[V]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(1)

print(count - 1)
