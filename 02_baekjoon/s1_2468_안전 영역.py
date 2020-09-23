# https://www.acmicpc.net/problem/2468
from itertools import product
import sys

sys.setrecursionlimit(100000)

dvecs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input().strip())
area = []
visit = [[0] * n for _ in range(n)]
mx = 0
for _ in range(n):
    line = list(map(int, input().strip().split()))
    line_mx = max(line)
    if line_mx > mx:
        mx = line_mx
    area.append(line)


def dfs(y, x):
    global rain
    visit[y][x] = 1
    for dy, dx in dvecs:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n):
            continue
        if not visit[ny][nx] and area[ny][nx] > rain:
            dfs(ny, nx)


mx_safe = 0
for rain in range(mx):
    n_safe = 0
    visit = [[0] * n for _ in range(n)]
    for i, j in product(range(n), range(n)):
        if not visit[i][j] and area[i][j] > rain:
            n_safe += 1
            dfs(i, j)
    # print(rain, n_safe)
    if n_safe > mx_safe:
        mx_safe = n_safe

print(mx_safe)
