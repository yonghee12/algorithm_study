# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    for new_node, linked in enumerate(graph[node]):
        if visited[new_node] or not linked:
            continue
        dfs(new_node)


n, m = map(int, input().strip().split(' '))
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().strip().split(' '))
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0 for _ in range(n + 1)]
ans = 0
for node in range(1, n + 1):
    if not visited[node]:
        dfs(node)
        ans += 1

print(ans)
