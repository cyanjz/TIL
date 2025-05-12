from collections import deque
import sys
sys.stdin = open('sample_input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def get_initial_positions():
    start_pos, end_pos = False, False
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start_pos = (r, c)
            elif arr[r][c] == 'Y':
                end_pos = (r, c)
    return start_pos, end_pos


def solve():
    q = deque()
    start_pos, end_pos = get_initial_positions()
    visited = [[[0] * N for _ in range(N)] for __ in range(K)]
    visited[K-1][start_pos[0]][start_pos[1]] = 1
    # cr, cc, face, K, turn
    q.append((start_pos[0], start_pos[1], 0, K, 0))
    while q:
        cr, cc, face, k, turn = q.popleft()
        for i in range(-1, 3):
            dr, dc = ds[(face+i)%4]
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'T':
                    if k:
                        for j in range(k-2, K):
                            if visited[j][nr][nc] <= turn+abs(i)+1:
                                continue
                        q.append((nr, nc, (face+i)%4, k-1, turn+abs(i)+1))
                        visited[k-2][nr][nc] = turn+abs(i)+1
                else:
                    for j in range(k-1, K):
                        if visited[j][nr][nc] <= turn+abs(i)+1:
                            continue
                    q.append((nr, nc, (face+i)%4, k, turn+abs(i)+1))
                    visited[k-1][nr][nc] = turn+abs(i)+1
    return max([visited[l][end_pos[0]][end_pos[1]]] for l in range(K))



ds = ((-1, 0), (0, 1), (1, 0), (0, -1))
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{t+1}', solve())