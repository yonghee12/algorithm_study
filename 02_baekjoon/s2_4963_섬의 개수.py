# https://www.acmicpc.net/problem/4963
# 23분. 평범한 flood fill 문제였지만 대각선이 추가.

import sys

sys.setrecursionlimit(10000)

from collections import deque

dvecs = [(1, 0), (0, 1), (-1, 0), (0, -1),
         (1, 1), (-1, 1), (-1, -1), (1, -1)]


def dfs(y, x):
    visit[y][x] = 1
    for dy, dx in dvecs:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < h and 0 <= nx < w):
            continue
        if not visit[ny][nx] and world[ny][nx]:
            dfs(ny, nx)


def dfs2(sy, sx):
    queue = deque([(sy, sx,)])
    while queue:
        y, x = queue.popleft()
        visit[y][x] = 1
        for dy, dx in dvecs:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if not visit[ny][nx] and world[ny][nx]:
                queue.append((ny, nx,))


while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break
    world = []
    visit = [[0] * w for _ in range(h)]
    for _ in range(h):
        line = map(int, input().strip().split())
        world.append(list(line))
    lands = 0
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and world[i][j]:
                lands += 1
                dfs2(i, j)
    print(lands)
