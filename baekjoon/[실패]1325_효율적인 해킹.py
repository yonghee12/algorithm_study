# https://www.acmicpc.net/problem/1325

import sys

sys.setrecursionlimit(100000000)

N, M = map(int, input().split())
graph = {k: [] for k in range(1, N + 1)}
counts = {k: 0 for k in range(1, N + 1)}
for _ in range(M):
    i, j = map(int, input().split())
    graph[j].append(i)


def dfs(node):
    visited[node] = 1
    if not graph[node]:
        return 0
    else:
        for n in graph[node]:
            if not visited[n]:
                dfs(n)


for v in graph.keys():
    visited = [0 for _ in range(0, N + 1)]
    dfs(v)
    counts[v] = sum(visited)

counts = sorted(counts.items(), key=lambda x: x[0], reverse=False)  # key로 오름차순 먼저 정렬 (우선순위 2)
counts = sorted(counts, key=lambda x: x[1], reverse=True)  # val 내림차순 정렬 (우선순위 1)
bigs = [counts[0][0]]
big_val = counts[0][1]
for k, v in counts[1:]:
    if v >= big_val:
        bigs.append(k)
print(' '.join(map(str, bigs)))
