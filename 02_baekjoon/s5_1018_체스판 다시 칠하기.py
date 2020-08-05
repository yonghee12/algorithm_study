# https://www.acmicpc.net/problem/1018

b1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
b2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


def check(label, pred):
    loss = 0
    for i in range(8):
        for j in range(8):
            loss += int(label[i][j] != pred[i][j])
    return loss


def get_bigboard():
    n, m = map(int, input().strip().split())
    bigboard = []
    for _ in range(n):
        bigboard.append(input().strip())
    return n, m, bigboard


def main():
    n, m, bigboard = get_bigboard()
    reversemax = -(n * m)
    for i in range(n - 7):
        for j in range(m - 7):
            board = [row[j:j + 8] for row in bigboard[i:i + 8]]
            localmax = max(-check(b1, board), -check(b2, board))
            if reversemax < localmax:
                reversemax = localmax
    print(-reversemax)


if __name__ == '__main__':
    main()
