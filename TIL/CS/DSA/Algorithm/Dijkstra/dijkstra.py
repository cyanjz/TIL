import heapq
import sys

sys.stdin = open('dijkstra_graph.txt', 'r')


def dijkstra(start):
    q = [(0, start)]
    D = [float('inf')] * V
    D[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if D[node] < cost:
            continue
        for n_w, next_node in adj_list[node]:
            next_cost = n_w + D[node]
            if D[next_node] <= next_cost:
                continue
            D[next_node] = next_cost
            heapq.heappush(q, (next_cost, next_node))
    return D


V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj_list[s].append((w, e))
print(dijkstra(0))
