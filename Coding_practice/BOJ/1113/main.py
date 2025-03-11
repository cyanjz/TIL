from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def bfs(cr, cc, ch):
    global max_height
    q = deque([(cr, cc)])
    volume = 0
    visited = [[0] * M for _ in range(N)]
    visited[cr][cc] = ch
    while q:
        cr, cc = q.popleft()
        volume += ch - arr[cr][cc]
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            # nr, nc가 수영장을 벗어나는 경우에는 즉시 return
            if not(0 <= nr < N and 0 <= nc < M):
                return False
            if not visited[nr][nc] and arr[nr][nc] < ch:
                visited[nr][nc] = ch
                q.append((nr, nc))
    for n in range(N):
        for m in range(M):
            max_height[n][m] = max(visited[n][m], max_height[n][m])
    return True


# 2500 * 9 ~ 25000-2500 = 22500
ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = 0
max_height = [[0] * M for _ in range(N)]
for h in range(9, 1, -1):
    for r in range(N):
        for c in range(M):
            if h > arr[r][c] and not max_height[r][c]:
                cur_v = bfs(r, c, h)

ans = 0
for r in range(N):
    for c in range(M):
        if max_height[r][c]:
            ans += max_height[r][c] - arr[r][c]
print(ans)
# for row in max_height:
#     print(*row)
