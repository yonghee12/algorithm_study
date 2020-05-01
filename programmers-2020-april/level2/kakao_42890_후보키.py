# https://programmers.co.kr/learn/courses/30/lessons/42890
# 참패한 문제. 정답률 16%
'''
시간 1.5시간 넘게 쓰고 반례 못 찾아서 대패.
패배 원인은 bfs 로직 생각하고 너무 심취해서 의심하지 않음
bfs에 큰 결함이 있었음. 물론 이것은 bfs dfs 등 탐색에 대한 근본적인 학습이 덜 된것에도 기인
우선 탐색부분에 힘을 쏟아야 하고 나중에 비트연산과 조합에 대해서, 그리고 집합에 대해 더 봐야함
'''


from collections import deque


def solution(relation):
    n_rows, n_cols = len(relation), len(relation[0])
    q = deque([[i] for i in range(n_cols)])
    answer = 0

    uniques = []
    while q:
        indices = q.popleft()
        search = [tuple(row[i] for i in indices) for row in relation]
        if len(set(search)) == n_rows:
            uniques.append(indices)
        q.extend([indices + [add_i] for add_i in range(indices[-1] + 1, n_cols)])
    uniques = sorted(uniques, key=lambda x: len(x), reverse=True)
    answer = 0
    for i in range(len(uniques)):
        if sum([set(uniques[i] + smallsets) == set(uniques[i]) for smallsets in uniques[i + 1:]
                if i < len(uniques) - 1]) == 0:
            answer += 1
    return answer


r = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
r = [['a', 'b', 'c'], ['1', 'b', 'c'], ['a', 'b', '4'], ['a', '5', 'c']]
r = [['a', '1', '4'], ['2', '1', '5'], ['a', '2', '4']]
r = [['ab', 'c'],
     ['a', 'bc'],
     ['x', 'yz'],
     ['x', 'c']]
r = [['a', '1'],
     ['a', '2']]
# 반례발견@!@!!!!!@!@!@!@!@!@!@!@!@
solution(r)
