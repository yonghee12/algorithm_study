# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(1500)
sys.stdin = open('input.in', 'r')


import sys
sys.setrecursionlimit(10000)
class Cabbage:
    def __init__(self):
        self.vec = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.w, self.h, self.n = map(int, input().split())
        self.board = [[0 for _ in range(self.w + 2)] for _ in range(self.h + 2)]
        self.check = [[0 for _ in range(self.w + 2)] for _ in range(self.h + 2)]

    def main(self):
        for _ in range(self.n):
            x, y = map(int, input().split())
            self.board[y + 1][x + 1] = 1
        ans = 0
        for i in range(1, self.h + 1):
            for j in range(self.w + 1):
                if self.board[i][j] and not self.check[i][j]:
                    self.dfs(i, j)
                    ans += 1
        print(ans)

    def dfs(self, y, x):
        self.check[y][x] = 1
        for i in range(4):
            yy, xx = y + self.vec[i][0], x + self.vec[i][1]
            if self.board[yy][xx] and not self.check[yy][xx]:
                self.dfs(yy, xx)


n_tests = int(input())
for _ in range(n_tests):
    cabbage = Cabbage()
    cabbage.main()