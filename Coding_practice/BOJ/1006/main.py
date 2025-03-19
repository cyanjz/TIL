import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('o.txt', 'w')
sys.setrecursionlimit(20000)


def get_neigh(r, c):
    cur_w = defence_center[r][c]
    result = []
    for func in funcs:
        nr, nc = func((r, c))
        n_w = defence_center[nr][nc]
        if n_w + cur_w <= W:
            result.append((nr, nc))
    return result


# 0. 인자
#   1) remaining : 남은 구역의 수
#   2) num_sf : 특수 부대의 수
#   3) cursor : 현재 보고 있는 위치
#   4) visited : 현재 위치를 sf가 커버하는지 여부
# 1. 종료 조건
#   1) basic : remaining = 0
#   2) pruning : num_sf >= ans
# 2. 재귀 호출
#   1) 현재 위치에 파견이 완료된 경우에는 cursor 1증가
#   2) 파견이 안된 경우에는 주변 칸들을 보고 가능한 경우에 대해서 다 호출.
def solve(remain, num_sf, cursor, visited):
    global ans
    if num_sf >= ans:           # 1-2) pruning
        return
    elif remain == 0:           # 1-1) basic
        ans = num_sf
        return
    elif visited & (1 << cursor):                     # 현재 위치에 이미 파견됨
        solve(remain, num_sf, cursor+1, visited)      # recursive call
    else:                                             # 현재 위치에 파견 안됨
        # case 1. 그냥 그 위치에만 파견
        solve(remain - 1, num_sf + 1, cursor + 1, visited + (1 << cursor))
        # case 2. 주변 탐색
        cr, cc = divmod(cursor, N)
        for nr, nc in neighs[cr][cc]:
            n_cursor = (nr * N + nc)
            if visited & 1 << n_cursor:               # 이웃을 방문한 적 있으면 skip
                continue
            next_visited = visited + (1 << cursor) + (1 << n_cursor)
            solve(remain - 2, num_sf + 1, cursor + 1, next_visited)


funcs = (lambda x: (x[0], (x[1]-1+N) % N),
         lambda x: (x[0] ^ 1, x[1]),
         lambda x: (x[0], (x[1]+1+N) % N))
# 일단 완전 탐색으로 풀어보기.
T = int(input())
for t in range(T):
    N, W = map(int, input().split())
    defence_center = [list(map(int, input().split())) for _ in range(2)]
    neighs = [[None] * N for _ in range(2)]
    for r in range(2):
        for c in range(N):
            neighs[r][c] = get_neigh(r, c)
    ans = 2*N
    solve(2*N, 0, 0, 1 << (2*N))
    print(ans)
