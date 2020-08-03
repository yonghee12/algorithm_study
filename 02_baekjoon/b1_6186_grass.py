# https://www.acmicpc.net/problem/6186
import sys

sys.setrecursionlimit(100000)


def read():
    return sys.stdin.readline().rstrip()


vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]

r, c = [int(i) for i in read().split(" ")]
field = [[0 for _ in range(c)] for _ in range(r)]
check = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j, char in enumerate(read()):
        if char == '#':
            field[i][j] = 1


def dfs(y, x):
    check[y][x] = 1
    for dv in vec:
        ny, nx = y + dv[0], x + dv[1]
        range_chk = 0 <= ny < r and 0 <= nx < c
        if range_chk:
            if field[ny][nx] and not check[ny][nx]:
                dfs(ny, nx)


ans = 0
for y in range(r):
    for x in range(c):
        if field[y][x] and not check[y][x]:
            dfs(y, x)
            ans += 1

print(ans)


