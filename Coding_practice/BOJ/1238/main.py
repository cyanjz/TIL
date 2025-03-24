import heapq
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def dijkstra(adj):
    queue = [(0, X)]
    D = [float('inf')] * N
    D[X] = 0
    while queue:
        cur_time, cur_node = heapq.heappop(queue)
        if D[cur_node] < cur_time:
            continue
        for next_time, next_node in adj[cur_node]:
            next_cost = D[cur_node] + next_time
            if D[next_node] <= next_cost:
                continue
            D[next_node] = next_cost
            heapq.heappush(queue, (next_cost, next_node))
    return D


N, M, X = map(int, input().split())
X -= 1
adj_mat = [[] for _ in range(N)]
rev_mat = [[] for _ in range(N)]
for _ in range(M):
    s, e, t = map(int, input().split())
    adj_mat[s-1].append((t, e-1))
    rev_mat[e-1].append((t, s-1))
D1 = dijkstra(adj_mat)
D2 = dijkstra(rev_mat)
print(max(x+y for x, y in zip(D1, D2)))
