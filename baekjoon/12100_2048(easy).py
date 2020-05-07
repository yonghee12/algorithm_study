# https://www.acmicpc.net/problem/12100
'''

'''
from copy import deepcopy
import sys
sys.setrecursionlimit(1000000)


def read():
    return sys.stdin.readline().strip()

class Game:
    def __init__(self):
        self.N = int(read())
        self.board = [list(map(int, read().split())) for _ in range(self.N)]

    def gravity_y(self, y_sign):
        for x in range(0, self.N):
            nonzeros = [self.board[y][x] for y in range(0, self.N)[::y_sign] if self.board[y][x]]
            fill = nonzeros + [0 for _ in range(self.N - len(nonzeros))]
            for y, f in zip(range(self.N)[::y_sign], fill):
                self.board[y][x] = f

    def gravity_x(self, x_sign):
        for y in range(0, self.N):
            nonzeros = [self.board[y][x] for x in range(0, self.N)[::x_sign] if self.board[y][x]]
            fill = nonzeros + [0 for _ in range(self.N - len(nonzeros))]
            for x, f in zip(range(self.N)[::x_sign], fill):
                self.board[y][x] = f

    def move_x(self, x_sign):
        self.gravity_x(x_sign)
        for y in range(self.N):
            for x in list(range(self.N - 1)):
                xx = -(x+1) if x_sign < 0 else x
                if self.board[y][xx] == self.board[y][xx + x_sign]:
                    self.board[y][xx] *= 2
                    self.board[y][xx + x_sign] = 0
        self.gravity_x(x_sign)

    def move_y(self, y_sign):
        self.gravity_y(y_sign)
        for x in range(self.N):
            for y in range(self.N - 1):
                yy = -(y + 1) if y_sign < 0 else y
                if self.board[yy][x] == self.board[yy + 1][x]:
                    self.board[yy][x] *= 2
                    self.board[yy + 1][x] = 0
        self.gravity_y(y_sign)


class Play:
    def __init__(self):
        self.vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.game = Game()
        self.biggest = 0

    def move(self, dy, dx):
        if dy != 0:
            self.game.move_y(dy)
        else:
            self.game.move_x(dx)
        return self.game.board

    def dfs(self, board, depth):
        biggest = max([max(row) for row in board])
        if depth == 0:
            return biggest
        else:
            for dy, dx in self.vec:
                self.game.board = deepcopy(board)
                if self.move(dy, dx) != board:
                    biggest = max(biggest, self.dfs(self.game.board, depth - 1))
            return biggest

play = Play()
print(play.dfs(play.game.board, 5))