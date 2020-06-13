# https://www.acmicpc.net/problem/1260

import sys

sys.setrecursionlimit(10000000)

from collections import deque


def read():
    return sys.stdin.readline().strip()


N, M, V = map(int, read().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    i, j = map(int, read().split())
    graph[i].append(j)
    graph[j].append(i)
for k, v in graph.items():
    graph[k] = sorted(v)


def bfs():
    q = deque(graph[V])
    visited = [0 for _ in range(N + 1)]
    visited[V] = 1
    searched = [V]
    while q:
        node = q.popleft()
        if not visited[node]:
            visited[node] = 1
            searched.append(node)
            to_queue = [neighbor for neighbor in graph[node] if not visited[neighbor]]
            q.extend(to_queue)
    return ' '.join(map(str, searched))


def dfs(node):
    dfs_stack.append(node)
    if not graph[node]:
        pass
    else:
        for new_node in graph[node]:
            if new_node not in dfs_stack:
                dfs(new_node)


dfs_stack = []
dfs(V)
print(' '.join(map(str, dfs_stack)))
print(bfs())
