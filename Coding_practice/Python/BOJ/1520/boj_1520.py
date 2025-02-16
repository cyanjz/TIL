dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

# BFS method
def solve():
    M, N = map(int, input().split())
    world_map = [list(map(int, input().split())) for _ in range(M)]
    DP_map = [[0] * N for _ in range(M)]
    DP_map[0][0] = 1
    q = [(0, 0)]

    while q:
        cr, cc = q.pop(0)
        ch = world_map[cr][cc]
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr <= M-1 and 0 <= nc <= N-1:
                if world_map[nr][nc] < ch:
                    q.append((nr, nc))
                    DP_map[nr][nc] += 1
    pm(DP_map)
    return DP_map[-1][-1]


def input():
    return f.readline().rstrip('\n')

def pm(world):
    for row in world:
        print(" ".join([f'{c}' for c in row]))

if __name__ == '__main__':
    with open(r'C:\DEV\personal\coding_test\BOJ\1520\test.txt', 'r') as f:
        print(solve())