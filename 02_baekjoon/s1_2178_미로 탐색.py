# https://www.acmicpc.net/problem/2178
# 30분 소요. bfs 문제.
# 1) history를 set으로 만들어서 history에 있었는지(본인 경로에 존재했는지 판별)
# 2) 지나온 경로는 도착경로 distance를 더해줌

from collections import deque

dvecs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append([int(i) for i in input()])


def bfs1():
    queue = deque([(0, 0, 1, set())])
    while queue:
        node = queue.popleft()
        y, x, dist, hist = node
        if y == n - 1 and x == m - 1:
            return dist
        for dy, dx in dvecs:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            if (ny, nx,) in hist:
                continue
            if miro[ny][nx]:
                hist.add((ny, nx,))
                queue.append((ny, nx, dist + 1, hist))


def bfs2():
    queue = deque([(0, 0, 1,)])
    while queue:
        node = queue.popleft()
        y, x, dist = node
        if y == n - 1 and x == m - 1:
            return dist
        for dy, dx in dvecs:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            if miro[ny][nx] == 1:
                miro[ny][nx] = miro[y][x] + 1
                queue.append((ny, nx, dist + 1))


print(bfs1())
