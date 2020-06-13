# https://programmers.co.kr/learn/courses/30/lessons/17679
'''
정답률 48.01%
43분 소요
짠 것중 가장 더럽게 짜서 기분이 안좋다..
'''


# 최초 풀이
def solution(m, n, board):
    cols = [
        [board[j][i] for j in range(m - 1, -1, -1)]
        for i in range(n)
    ]
    answer = 0

    while True:
        squares = []
        for i in range(n - 1):
            col = cols[i]
            nextcol = cols[i + 1]
            for j in range(m - 1):
                current = col[j]
                if current == " ":
                    continue
                if current == col[j + 1] and current == nextcol[j] and current == nextcol[j + 1]:
                    squares.extend([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
        if not squares:
            return answer
        else:
            squares = list(sorted(set(squares)))
            for i in range(n):
                newcol = []
                for j in range(m):
                    if (i, j) not in squares:
                        newcol.append(cols[i][j])
                    else:
                        answer += 1
                cols[i] = list(''.join(newcol).ljust(m))


# OOP 풀이
class Game:
    def __init__(self, m, n, board):
        self.m = m
        self.n = n
        self.board = [[board[j][i] for j in range(m - 1, -1, -1)]
                      for i in range(n)]
        self.answer = 0
        self.sqaures = None

    def find_squares(self):
        squares = []
        n, m, cols = self.n, self.m, self.board
        for i in range(n - 1):
            col = cols[i]
            nextcol = cols[i + 1]
            for j in range(m - 1):
                current = col[j]
                if current == " ":
                    continue
                if current == col[j + 1] and current == nextcol[j] and current == nextcol[j + 1]:
                    squares.extend([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])
        self.sqaures = squares
        return squares

    def bomb_squares(self):
        n, m, cols, squares = self.n, self.m, self.board, self.sqaures
        squares = list(sorted(set(squares)))
        for i in range(n):
            newcol = []
            for j in range(m):
                if (i, j) not in squares:
                    newcol.append(cols[i][j])
                else:
                    self.answer += 1
            cols[i] = list(''.join(newcol).ljust(m))
        self.board = cols
        return self.board


def solution(m, n, board):
    game = Game(m, n, board)
    while True:
        if not game.find_squares():
            return game.answer
        else:
            game.bomb_squares()


board1 = ['TTTANT',
          'RRFACC',
          'RRRFCC',
          'TRRRAA',
          'TTMMMF',
          'TMMTTJ']

board2 = ['CCBDE',
          'AAADE',
          'AAABF',
          'CCBBF']

solution(4, 5, board2)
