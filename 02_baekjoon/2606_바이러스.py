# https://www.acmicpc.net/problem/2606

N = int(input())
graph = {k: [] for k in range(1, N + 1)}
for _ in range(int(input())):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
visited = [0 for _ in range(N + 1)]

def dfs(node, depth):
    for n in graph[node]:
        if not visited[n]:
            visited[n] = 1
            dfs(n, depth + 1)

from collections import deque

def bfs():
    q = deque([1])
    while q:
        node = q.popleft()
        visited[node] = 1
        q.extend([n for n in graph[node] if not visited[n]])

# dfs(1, 0)
bfs()
print(sum(visited) - 1)
