from collections import deque


def bfs():
    rear = 0
    front = -1
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while rear != front:
        front += 1
        cr, cc = q[front]
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc] != 1:
                if nr == N-1 and nc == M-1:
                    return visited[cr][cc] + 1
                rear += 1
                q[rear] = (nr, nc)
                visited[nr][nc] = visited[cr][cc] + 1
    return MAX_DIST


def pa(arr):
    print()
    print('#' * M)
    for row in arr:
        print(*row)


def solve_bf():
    global maze
    ans = MAX_DIST
    for r in range(N):
        for c in range(M):
            if maze[r][c] == 1:
                maze[r][c] = 0
                ans = min(bfs(), ans)
                maze[r][c] = 1
    ans = min(bfs(), ans)
    if ans == MAX_DIST:
        return -1
    return ans


def solve():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, 1)])
    visited[0][0][1] = 1
    while q:
        cr, cc, power = q.popleft()
        if cr == N-1 and cc == M-1:
            return visited[cr][cc][power]
        for dr, dc in ds:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == 1 and power:
                    visited[nr][nc][0] = visited[cr][cc][power] + 1
                    q.append((nr, nc, 0))
                elif maze[nr][nc] == 0 and visited[nr][nc][power] == 0:
                    visited[nr][nc][power] = visited[cr][cc][power] + 1
                    q.append((nr, nc, power))
    return -1


if __name__ == "__main__":
    ds = ((1, 0), (-1, 0), (0, 1), (0, -1))
    N, M = map(int, input().split())
    MAX_DIST = N*M+1
    maze = [list(map(int, input())) for _ in range(N)]
    print(solve())
