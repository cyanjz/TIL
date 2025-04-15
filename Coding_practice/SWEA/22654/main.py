import sys
sys.stdin = open('sample_input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def solve():
    C, cmd_list = input().split()
    C = int(C)
    face = 0
    cr, cc = start_pos
    for c in range(C):
        cmd = cmd_list[c]
        if cmd == 'R':
            face = (face + 1)%4
        elif cmd == 'L':
            face = (face - 1)%4
        else:
            dr, dc = ds[face]
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 'T':
                cr, cc = nr, nc
    if (cr, cc) == end_pos:
        return 1
    return 0


# 상우하좌
ds = [
    (-1, 0), 
    (0, 1), 
    (1, 0),
    (0, -1)
]
T = int(input())
for t in range(T):
    # read input
    N = int(input())
    arr = [input() for _ in range(N)]
    # find start position & end position
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start_pos = (r, c)
            elif arr[r][c] == 'Y':
                end_pos = (r, c)
    # run solve Q times
    Q = int(input())
    ans = [solve() for q in range(Q)]
    print(f'#{t+1}', *ans)