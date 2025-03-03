from collections import deque


def tilt_right(candies):
    # 오른쪽 먼저.
    candies.sort(key=lambda x: -x[1])  # 내림차순 정렬. col이 큰쪽을 먼저 해야함.
    result = []
    arrived = False
    r, c, color = candies[0]
    nr, nc = r, c + 1
    while arr[nr][nc] == '.' and nr != candies[1][0] and nc != candies[1][1]:
        nc += 1
    if arr[nr][nc] == 'O':  # 도착.
        pass
    else:
        result.append((nr, nc-1, color))
    r, c, color = candies[1]
    nr, nc = r, c + 1
    while arr[nr][nc] == '.' and nr != candies[1][0] and nc != candies[1][1]:
        nc += 1
    if arr[nr][nc] == 'O':  # 도착.
        pass
    else:
        result.append((nr, nc-1, color))
    return


def solve():
    global candies
    q = deque([candies])
    while q:
        candies = q.popleft()
        for candy in candies:
            for tilt in tilts:

    return


if __name__ == '__main__':
    # read array and find the locations of red and blue candies
    N, M = map(int, input().split())
    # . 빈칸, # 벽, B 파란사탕, R 빨간사탕, O 출구.
    arr = [[0] * M for _ in range(N)]
    candies = [None, None]  # candies : (r, c, color). color -> 0 : blue, 1 : red
    cnt = 0
    min_cnt = 10
    visited = []
    d_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(N):
        row = input()
        for c in range(M):
            if row[c] == 'B':
                candies[0] = (r, c, 0)
                arr[r][c] = '.'
            elif row[c] == 'R':
                candies[1] = (r, c, 1)
                arr[r][c] = '.'
            else:
                arr[r][c] = row[c]
    tilts = [tilt_left, tilt_right, tilt_up, tilt_down]
    solve()
