def solve():
    ans = 0
    C, R = map(int, input().split())
    matures = []
    num_zeros = 0
    tomatos = [[0] * C for _ in range(R)]
    for r in range(R):
        line = list(map(int, input().split()))
        for c in range(C):
            if line[c] == 1:
                tomatos[r][c] = 1
                matures.append((r, c))
            elif line[c] == -1:
                tomatos[r][c] = -1
            else:
                num_zeros += 1
    while matures:
        next_matrues = []
        for mr, mc in matures:
            for dr, dc in ds:
                nr, nc = mr + dr, mc + dc
                if 0 <= nr < R and 0 <= nc < C and not tomatos[nr][nc]:
                    next_matrues.append((nr, nc))
                    tomatos[nr][nc] = 1
                    num_zeros -= 1
        matures = next_matrues
        ans += 1
    if num_zeros:
        return -1
    return ans - 1


ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print(solve())
