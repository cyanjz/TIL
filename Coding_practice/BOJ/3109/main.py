def dfs(cr, cc):
    global ans
    if cc == C-1:
        visited[cr][cc] = 1
        ans += 1
    else:
        visited[cr][cc] = 1
        for dr, dc in ds:
            nr, nc = cr + dc, cc + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] != 'x' and not visited[nr][nc]:
                    dfs(nr, nc)
        visited[cr][cc] = 0


ds = [[-1, 1], [0, 1], [1, 1]]
R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]
arr = [input() for _ in range(R)]
ans = 0
for r in range(R):
    if arr[r][0] == '.':
        dfs(r, 0)
print(ans)