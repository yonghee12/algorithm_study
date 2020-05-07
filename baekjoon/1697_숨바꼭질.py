# https://www.acmicpc.net/problem/1697
'''
ㅎㅎ
이 문제의 패인은
우선 큐에서 꺼냈을 때는 '처리된 것'이어야 한다는걸 몰랐고 (depth 때문)
그래서 동일한 점일 때 방문 또하게 되어 테스트 케이스를 틀렸다.
'''


from collections import deque

N, K = map(int, input().strip().split())


MAX = 100001


def walk_b(x):
    return x - 1


def walk_f(x):
    return x + 1


def trans(x):
    return 2 * x


def bfs():
    choices = [walk_b, walk_f, trans]
    q = deque()
    q.extend([{'depth': 0, 'pos': N}])
    visited = {}
    while q:
        node = q.popleft()
        pos = node['pos']
        visited[pos] = True
        if pos == K:
            return node['depth']
        else:
            for f in choices:
                new_pos = f(pos)
                if 0 <= new_pos < MAX and not visited.get(new_pos):
                    q.extend([{'depth': node['depth'] + 1, 'pos': new_pos}])


visited = [0 for _ in range(MAX)]
def bfs2():
    q = deque([N])
    while q:
        pos = q.popleft()
        if pos == K:
            return visited[pos]
        else:
            for next_pos in [pos - 1, pos + 1, pos * 2]:
                if 0 <= next_pos < MAX and not visited[next_pos]:
                    visited[next_pos] = visited[pos] + 1
                    q.append(next_pos)


print(bfs())