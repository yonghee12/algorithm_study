from collections import deque

def update(o, p, graph):
    if graph.get(o):
        graph[o].append(p)
    else:
        graph[o] = [p]
    return graph

def solution(n, path, order):
    graph = {}
    for o, p in path:
        graph = update(o, p, graph)
        graph = update(p, o, graph)
    orders = {}
    for o, p in order:
        orders[p] = o
        # orders = update(p, o, orders)

    # orderkeys = {k: 1 for k in graph.keys() if orders.get(k)}
    nonorders = {k: 1 for k in graph.keys() if orders.get(k) is None}
    visited = [0 for _ in range(n+1)]
    visit_order = []
    q = deque([0])
    while q:
        print(q)
        node = q.popleft()
        visited[node] = 1
        visit_order.append(node)
        for k in graph[node]:
            print(k)
            if nonorders.get(k):
                q.append(k)
            elif orders.get(k):
                if visited[orders[k]] == 1:
                    q.append(k)
    print(visit_order)
    if sum(visited) == n:
        return True
    else:
        return False

                # if order[k]
        # visited[node] = 1





    answer = True
    return answer

n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]
solution(n, path, order)
