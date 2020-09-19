# https://www.acmicpc.net/problem/11403
# 소요시간 50분
# index인지 value인지 헛갈리며 시간 잡아먹음
# linked list (or hash) 형태가 아닌 adjacent matrix 형태 익숙하지 않음을 드러냄

import sys

sys.setrecursionlimit(100000)

n = int(input())
res = [[0] * n for _ in range(n)]
mat = [[0] * n for _ in range(n)]
for i in range(n):
    line = input().split()
    for j in range(n):
        mat[i][j] = int(line[j])


def dfs(node):
    global visited
    global res
    visited.add(node)
    for i in range(n):
        if mat[node][i] and i not in visited:
            dfs(i)


for i in range(n):
    startnodes = []
    for j in range(n):
        if mat[i][j] == 1:
            res[i][j] = 1
            startnodes.append(j)
    visited = set()

    for startnode in startnodes:
        if startnode in visited:
            continue
        dfs(startnode)
    for visit in visited:
        res[i][visit] = 1

print('\n'.join([' '.join(map(str, row)) for row in res]))
