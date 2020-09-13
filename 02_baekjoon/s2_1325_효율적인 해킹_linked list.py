# https://www.acmicpc.net/problem/1325
"""
간선의 갯수가 directed graph 최대 갯수인 약 일억보다 훨씬 작은 십만개로 sparse graph가 예상됨
따라서 linked list로 먼저 접근
"""

import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
# starts = [0 for _ in range(n + 1)]
starts = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    starts.append(b)


max_depth = 0
for s in starts:
    depth = bfs(s, -1)
    max_depth = depth if depth > max_depth else max_depth
