# https://www.acmicpc.net/problem/1753

# 다익스트라 처음 짠 문제. 다익스트라 본체 로직은 맞았지만 문제에서 동일 경로에 여러 간선이 있을 수 있다고 한 것을 못봐서 시간초과.
# pypy는 이상하게 들어갔지만, 틀린 로직. 그래프 받을 때 min()을 써서 모든 경로에 대해 이미 최소 가중치를 가진 그래프로 시작하는게 핵심

import sys
import heapq

input = sys.stdin.readline
inf = 1e9


def main():
    V, E = map(int, input().split())
    k = int(input())

    graph = [dict() for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w

    def dijikstra2(graph, startnode):
        # distance 배열 초기화
        distances = [inf] * (V + 1)
        distances[startnode] = 0

        # heapq 이용 Priority Queue
        pq = []
        heapq.heappush(pq, (0, startnode,))

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if distances[current_node] < current_dist or not graph[current_node]:
                continue
            for new_node, new_weight in graph[current_node].items():
                new_dist = current_dist + new_weight
                if distances[new_node] < new_dist:
                    continue
                distances[new_node] = new_dist
                heapq.heappush(pq, (new_dist, new_node,))
        return distances

    distances = dijikstra2(graph, startnode=k)
    for dist in distances[1:]:
        if isinstance(dist, int):
            print(dist)
        else:
            print("INF")


if __name__ == '__main__':
    main()
