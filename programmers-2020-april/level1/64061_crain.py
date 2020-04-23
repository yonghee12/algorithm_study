# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def get_stack(board):
    board_stack = []
    for w in range(len(board)):
        col = []
        for h in range(len(board) - 1, -1, -1):
            doll = board[h][w]
            if doll == 0:
                break
            else:
                col.append(doll)
        board_stack.append(col)
    return board_stack


def solution(board, moves):
    board_stack = get_stack(board)

    basket = []
    answer = 0
    for move in moves:
        lane = move - 1
        if board_stack[lane]:
            picked = board_stack[lane].pop()

            if basket:
                if picked == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(picked)
            else:
                basket.append(picked)

    return answer