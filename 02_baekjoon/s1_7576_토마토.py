# https://www.acmicpc.net/problem/7576
# 30분 소요.
# 로직은 맞아

from collections import deque

dvecs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

m, n = map(int, input().split())
box = []
n_tomatoes = m * n
rottens = set()
for i in range(n):
    row = []
    for j, num in enumerate(input().split()):
        row.append(int(num))
        if num == '1':
            rottens.add((i, j,))
        if num == '-1':
            n_tomatoes -= 1
    box.append(row)


def bfs():
    n_rotten = 0
    queue = deque(rottens)
    while True:
        node = queue.popleft()
        y, x = node
        n_rotten += 1
        if n_rotten == n_tomatoes:
            return box[y][x] - 1
        for dy, dx in dvecs:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            if box[ny][nx] == 0:
                queue.append((ny, nx,))
                box[ny][nx] = box[y][x] + 1

        if not queue:
            if n_rotten < n_tomatoes:
                return -1
            else:
                return 0

print(bfs())

