# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def update_graph(p, q):
    if p in graph:
        graph[p].append(q)
    else:
        graph[p] = [q]


def dfs(node):
    visited[node] = 1
    for new_node in graph[node]:
        if not visited[new_node]:
            dfs(new_node)


n, m = map(int, input().strip().split(' '))
if m == 0:
    print(n)
else:
    graph = {}
    for _ in range(m):
        x, y = map(int, input().strip().split(' '))
        update_graph(x, y)
        update_graph(y, x)

    visited = [0 for _ in range(n + 1)]
    ans = 0
    nodes = list(graph.keys())
    for node in nodes:
        if not visited[node]:
            dfs(node)
            ans += 1
    remainders = n - len(nodes)
    print(ans + remainders)
