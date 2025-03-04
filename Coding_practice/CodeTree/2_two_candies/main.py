from collections import deque


def tilt(d, r, c):
    if r != goal_r or c != goal_c:
        while maze[r][c] == '.':
            r += d[0]
            c += d[1]
    return r, c


def get_neigh(blue_r, blue_c, red_r, red_c):
    # 오른쪽, 왼쪽, 위로, 아래
    ds = ((0, 1), (0, -1), (-1, 0), (0, -1))
    # color, direction, r/c
    arr = [[(N, M)] * 4 for _ in range(2)]
    top = -1
    for d in ds:
        top += 1
        arr[0][top] = list(tilt(d, blue_r, blue_c))
        arr[1][top] = list(tilt(d, red_r, red_c))
    # case 0 : goal reached
    for i in range(4):
        if arr[0][i] == (goal_r, goal_c) and arr[1][i] == (goal_r, goal_c):
            return
    # case 1 : return neigh
    if blue_r == red_r:
        if blue_c < red_c:                  # 빨간 사탕이 오른쪽에 있음.
            if arr[0][0][1] == arr[1][0][1]:
                arr[0][0][1] -= 1
            if arr[0][1][1] == arr[1][1][1]:
                arr[1][1][1] += 1
        else:                               # 빨간 사탕이 왼쪽에 있음.
            if arr[0][0][1] == arr[1][0][1]:
                arr[1][0][1] -= 1
            if arr[0][1][1] == arr[1][1][1]:
                arr[0][1][1] += 1
    if blue_c == red_c:
        if blue_r < red_r:                  # 빨간 사탕이 아래 있음.
            if arr[1][2][0] == arr[0][2][0]:
                arr[1][2][0] += 1
            if arr[0][3][0] == arr[1][3][0]:
                arr[0][3][0] -= 1
        else:                               # 빨간 사탕이 위에 있음.
            if arr[1][2][0] == arr[0][2][0]:
                arr[0][2][0] += 1
            if arr[0][3][0] == arr[1][3][0]:
                arr[1][3][0] -= 1
    print(arr)
    return arr


def solve(blue_r, blue_c, red_r, red_c):
    # shape : N X M X N X M
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[blue_r][blue_c][red_r][red_c] = 1
    q = deque([(blue_r, blue_c, red_r, red_c)])
    print(q)
    while q:
        print(1)
        try:
            blue_r, blue_c, red_r, red_c = q.popleft()
        except:
            breakpoint()
        neigh = get_neigh(blue_r, blue_c, red_r, red_c)
        cur_depth = visited[blue_r][blue_c][red_r][red_c]
        if neigh is None:
            return cur_depth + 1
        else:
            for blue_coord, red_coord in neigh:
                print(blue_coord, red_coord)
                n_blue_r, n_blue_c = blue_coord
                n_red_r, n_red_c = red_coord
                if not visited[n_blue_r][n_blue_c][n_red_r][n_red_c]:
                    q.append((n_blue_r, n_blue_c, n_red_r, n_red_c))
                    visited[n_blue_r][n_blue_c][n_red_r][n_red_c] = cur_depth + 1
    return -1


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
blue_r, blue_c, red_r, red_c, goal_r, goal_c = None, None, None, None, None, None

for r in range(N):
    for c in range(M):
        if maze[r][c] == 'B':
            blue_r, blue_c = r, c
            maze[r][c] = '.'
        elif maze[r][c] == 'R':
            red_r, red_c = r, c
            maze[r][c] = '.'
        elif maze[r][c] == 'O':
            goal_r, goal_c = r, c
        if blue_r and blue_c and red_r and red_c and goal_r and goal_c:
            break
solve(blue_r, blue_c, red_r, red_c)
