import heapq
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def dijkstra():
    queue = [(arr[0][0], 0, 0)]   # cost, r, c
    loss = [[float('inf')] * N for _ in range(N)]
    loss[0][0] = arr[0][0]
    while queue:
        cost, cr, cc = heapq.heappop(queue)
        if loss[cr][cc] < cost:
            continue
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                next_loss = loss[cr][cc] + arr[nr][nc]
                if loss[nr][nc] <= next_loss:
                    continue
                loss[nr][nc] = next_loss
                heapq.heappush(queue, (next_loss, nr, nc))
    return loss[-1][-1]


ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
t = 0
while True:
    N = int(input())
    if N == 0:
        break
    t += 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {t}: {dijkstra()}')
