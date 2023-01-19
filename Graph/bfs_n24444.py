import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(V):
    global count

    queue = deque([R])
    visited[R] = 1
    while queue:
        V = queue.popleft()
        graph[V].sort()
        for g in graph[V]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                queue.append(g)
bfs(R)

for v in visited[1:]:
    print(v)

