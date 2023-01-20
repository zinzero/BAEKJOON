from collections import deque

# 정점, 간선, 시작점
N, M, V = map(int, input().split())

# 인접 0행렬
matrix = [[0] * (N + 1) for i in range(N + 1)]

# 방문한 곳 체크 리스트
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

# 입력받는 값에 대해 0행렬 1삽입 (인접리스트 생성)
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    visited_dfs[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if visited_dfs[i] == 0 and matrix[V][i] == 1:
            dfs(i)

def bfs(V):
    queue = deque([V])
    visited_bfs[V] = 1

    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited_bfs[i] == 0 and matrix[V][i] == 1:
                queue.append(i)
                visited_bfs[i] = 1

dfs(V)
print()
bfs(V)
