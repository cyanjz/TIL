def solve():
    shark_size = 2
    shark_eat = 0
    fishes = 0
    shark_loc = [0, 0]
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 9:
                shark_loc = (r, c)
            elif arr[r][c] != 0:
                fishes += 1
    q = [0] * 101
    while fishes:
        # bfs
        front = -1
        rear = 0
        q = [rear] = shark_loc
        visited = [[0]*10 for _ in range(10)]
        visited[shark_loc[0]][shark_loc[1]] = 1
        while front != rear:
            front += 1
            cr, cc = q[front]
            for dr, dc in ds:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < 10 and 0 <= nc < 10 and arr[nr][nc] != 0 and not visited[nr][nc]:
                    if arr[nr][nc] < shark_size:
                        shark_eat += 1
                    rear += 1
                    q[rear] = (nr, nc)
                    visited[nr][nc] = 1
                    
    return


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    solve()
