def solve(sr, sc, d):
    visited = [[0] * m for _ in range(n)]
    visited[sr][sc] = 1
    cr, cc = sr, sc
    cnt = 1
    while True:
        # 각 방향별로 방문 가능 여부 판별
        for i in range(4):
            d = (d-1) % 4
            dr, dc = ds[d]
            nr, nc = cr + dr, cc + dc
            # 방문하지 않은 경우에
            if not visited[nr][nc] and arr[nr][nc] == 0:
                cr, cc = nr, nc
                visited[nr][nc] = 1
                cnt += 1
                break
        # 방문 가능한 경우가 없음
        else:
            # 한칸 후진 했을 때의 좌표
            nr, nc = cr - dr, cc - dc
            if arr[nr][nc] == 0:
                cr, cc = nr, nc
            else:
                break
        # print('#' * (2*m-1))
        # print(cr, cc, d)
        # for row in visited:
        #     print(*row)
    return cnt


# n, m -> row, col size
n, m = map(int, input().split())
# start_r, start_c, direction(북동남서)
start_r, start_c, start_d = map(int, input().split())
ds = ((-1, 0), (0, 1), (1, 0), (0, -1))
arr = [list(map(int, input().split())) for _ in range(n)]
print(solve(start_r, start_c, start_d))
