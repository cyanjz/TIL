def solve():
    cnt = 0
    # 2d arr to measure the number of on bulbs in neighbhors.
    bulb_arr = [[0] * 10 for _ in range(10)]
    for r in range(10):
        for c in range(10):
            temp = 0
            if arr[r][c] == 'O':
                cnt += 1
                temp += 1
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 10 and 0 <= nc < 10 and arr[nr][nc] == 'O':
                    temp += 1
            bulb_arr[r][c] = temp
    while cnt:
        pass
    return None


ds = ((1, 0), (0, 1), (-1, 0), (0, -1))
if __name__ == "__main__":
    arr = [list(map(int, input().split())) for _ in range(10)]
