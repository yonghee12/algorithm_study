# https://www.acmicpc.net/problem/2210

board = [input().split() for _ in range(5)]
vecs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
digits = set()


def dfs(y, x, digit):
    digit += board[y][x]
    if len(digit) == 6:
        digits.add(digit)
    else:
        for dy, dx in vecs:
            ny, nx = y + dy, x + dx
            if 0 <= ny <= 4 and 0 <= nx <= 4:
                dfs(ny, nx, digit)


for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(digits))
