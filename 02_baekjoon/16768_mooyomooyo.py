# https://www.acmicpc.net/problem/16768
'''
필요한 기능
* 한 탄
    * flood fill 체크하여 없앨것 정하기
        * dfs 사용
    * gravity 적용하여 터뜨린 후 아래로 내리기
'''

'''
얻어야 할 것
- 같은 작업을 영원히 돌려서 마지막을 출력 -> flag로 while문
- 백준은 stdin.readline()
- flood fill 후 갯수를 알아야 할 경우 : dfs에서 옆에 방향 돌기 전에 agg할 int 하나 있으면 됨
    -> 그럼 그 숫자를 어떻게 확신하느냐 : 애초에 조건이 아니면 dfs 들어가지 말도록 하면 됨 
- pull down 로직은 다음에도 쓸만한듯
'''
import sys

sys.setrecursionlimit(1000000)


def read():
    return sys.stdin.readline().strip()


class Mooyo:
    def __init__(self):
        self.vec = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.n, self.k = map(int, read().split())
        self.board = [list(map(int, list('0' + read() + '0'))) for _ in range(self.n)]
        self.board = [[0 for _ in range(12)]] + self.board + [[0 for _ in range(12)]]
        self.check = [[0 for _ in range(12)] for _ in range(self.n + 2)]
        self.dfs_stack = []

    def main(self):
        while True:
            changed = self.check_stage()
            if changed:
                self.pull_down()
            else:
                break
        self.print_board()

    def check_stage(self):
        changed = False
        self.check = [[0 for _ in range(12)] for _ in range(self.n + 2)]
        for i in range(1, self.n + 1):
            for j in range(1, 10 + 1):
                c = self.board[i][j]
                if c and not self.check[i][j]:
                    self.dfs_stack = []
                    adjacent = self.search_dfs(i, j)
                    if adjacent >= self.k:
                        changed = True
                        self.kill_adj()
                    self.dfs_stack = []
        return changed

    def search_dfs(self, y, x):
        self.check[y][x] = 1
        self.dfs_stack.append((y, x))
        adj = 1
        for i in range(4):
            yy, xx = y + self.vec[i][0], x + self.vec[i][1]
            if self.board[yy][xx] == self.board[y][x] and not self.check[yy][xx]:
                adj += self.search_dfs(yy, xx)
        return adj

    def kill_adj(self):
        for y, x in self.dfs_stack:
            self.board[y][x] = 0

    def pull_down(self):
        for j in range(1, 10 + 1):
            nonzeros = [self.board[i][j] for i in range(self.n, 0, -1) if self.board[i][j]]
            fill = nonzeros + [0 for _ in range(0, self.n - len(nonzeros))]
            for i, f in zip(range(self.n, 0, -1), fill):
                self.board[i][j] = f

    def print_board(self):
        for i in range(1, self.n + 1):
            print(''.join(map(str, self.board[i][1:-1])))


mooyo = Mooyo()
mooyo.main()
