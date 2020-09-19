import sys

sys.setrecursionlimit(10000)

dvecs = ((1, 0), (0, 1), (-1, 0), (0, -1))
n_marked = 0

n = int(input())
check = [[0] * n for _ in range(n)]
mat = []
for _ in range(n):
    mat.append([int(i) for i in input()])


def dfs(y, x):
    global n_marked
    check[y][x] = 1
    n_marked += 1
    for dy, dx in dvecs:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n):
            continue
        if mat[ny][nx] and not check[ny][nx]:
            dfs(ny, nx)


ans = []
for y in range(n):
    for x in range(n):
        if not check[y][x] and mat[y][x]:
            dfs(y, x)
            ans.append(n_marked)
            n_marked = 0

ans.sort(reverse=False)
print(len(ans))
for a in ans:
    print(a)