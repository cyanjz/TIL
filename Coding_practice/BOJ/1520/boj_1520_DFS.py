import sys
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
sys.setrecursionlimit(10**6)

# DFS - recursion method
def DFS(r, c):
    if r == M-1 and c == N-1:
        DP[r][c] = 1
        return 1
    if DP[r][c] != -1:
        return DP[r][c]
    else:
        x = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr <= M-1 and 0 <= nc <= N-1:
                if world_map[r][c] > world_map[nr][nc]:
                    x += DFS(nr, nc)
        DP[r][c] = x
        return DP[r][c]

# def pm(wm):
#     for row in wm:
#         print(' '.join([f'{x}' for x in row]))

# def input():
#     return f.readline().rstrip('\n')

if __name__ == '__main__':
    # with open(r'C:\DEV\personal\coding_test\BOJ\1520\test.txt', 'r') as f:
    M, N = map(int, input().split())
    world_map = [list(map(int, input().split())) for _ in range(M)]
    DP = [[-1] * N for _ in range(M)]
    DFS(0, 0)
    print(DP[0][0])