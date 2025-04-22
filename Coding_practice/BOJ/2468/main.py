# 가능한 모든 높이에 대하여 모든 점에 대하여 bfs 수행.
# 최악의 경우
# 100 * 100 * 10000 = 100000000
# 최대 150000000번이니 수행 가능함.
# 1. 모든 점들을 순회하면서 높이를 읽어오고 해당 높이에 대하여 시뮬레이션을 시행한 적이 없는 경우에는
#   arr의 모든 점들에 대하여 bfs를 수행.
# 2. call_bfs를 통해 모든 점들에 대하여 bfs를 수행.
#   1) bfs 수행 조건은, 현재 물 높이보다 큰 지역을 찾은 경우.
#   2) bfs를 돌리면서 visited 배열을 업데이트.
#   3) bfs를 돌리면 새로운 안전 구역을 찾은 것이므로 바로 안전 구역 개수 + 1
#   4) 또한, 방문한 경우에는 bfs 돌리지 않는다.
# 3. bfs 수행
#   1) bfs 조건은 일반적인 bfs 조건 + 인접한 칸의 높이가 물 높이보다 큰 경우
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def call_bfs(h):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            visited[r][c] = 1
            if arr[r][c] > h:
                bfs(r, c, h, visited)
                cnt += 1
    return cnt


def bfs(r, c, h, visited):
    q = deque()
    q.append((r, c))
    while q:
        cr, cc = q.popleft()
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] > h:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return


def solve():
    h_visited = [0] * 101
    ans = 1
    for r in range(N):
        for c in range(N):
            h = arr[r][c]
            # 탐색한 적이 없는 높이인 경우에
            if not h_visited[h]:
                ans = max(call_bfs(h), ans)
                h_visited[h] = 1
    return ans


ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solve())
