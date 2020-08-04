# https://www.acmicpc.net/problem/11650

import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
points = []
for _ in range(n):
    points.append(tuple(map(int, read().split(' '))))

sort = sorted(points, key=lambda x: (x[0], x[1]))
sys.stdout.write('\n'.join([' '.join(map(str, tup)) for tup in sort]))
