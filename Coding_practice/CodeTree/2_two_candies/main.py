# 문제 좀 잘 읽어라... 파란색은 빼면 안되잖아...
from collections import deque


def tilt(d, r, c):
    if r != goal_r or c != goal_c:
        while maze[r][c] == '.':
            r += d[0]
            c += d[1]
        if maze[r][c] == '#':
            r -= d[0]
            c -= d[1]
    return r, c


def get_neigh(blue_r, blue_c, red_r, red_c):
    # 오른쪽, 왼쪽, 위로, 아래
    ds = ((0, 1), (0, -1), (-1, 0), (1, 0))
    # color, direction, r/c
    arr = [[(N, M)] * 4 for _ in range(2)]
    top = -1
    for d in ds:
        top += 1
        arr[0][top] = list(tilt(d, blue_r, blue_c))
        arr[1][top] = list(tilt(d, red_r, red_c))
    # case 0 : goal reached
    # 빨강 파랑 둘 다 구멍에 도착한 경우에는 제외.
    for i in range(4):
        # r1, c1 = arr[0][i]
        # r2, c2 = arr[1][i]
        # pm(r1, c1, r2, c2)
        # end condition : 빨간색만 도달한 경우.
        if arr[0][i] != [goal_r, goal_c] and arr[1][i] == [goal_r, goal_c]:
            return
        # 파란색이 도달한 경우에는 파란색의 좌표를 None으로 설정.
        if arr[0][i] == [goal_r, goal_c]:
            arr[0][i] = [None, None]
    # case 1 : return neigh
    # 사탕이 같은 위치에 놓이는 경우는 사탕을 한칸 옮겨줘야 한다.
    # 그런데 위에서 파란 사탕과 빨간 사탕이 둘 다 도달한 경우에는 걸러줘야 하니
    # arr[0][i] == [goal_r, goal_c]인 경우에는 하면 안됨.
    # 위쪽에서 arr[0][i] == [goal_r, goal_c]인 경우에는 (None, None)으로 해줬으니
    # 아래쪽에서는 같은 경우가 없을 것.
    # 그러니 함수 밖에서 None, None인 경우에는 불가능한 케이스이므로 제외하면 됨.
    # right, left
    if blue_r == red_r:
        if blue_c < red_c:                  # 빨간 사탕이 오른쪽에 있음.
            if arr[0][0][1] == arr[1][0][1]:    # right
                arr[0][0][1] -= 1
            if arr[0][1][1] == arr[1][1][1]:    # left
                arr[1][1][1] += 1
        else:                               # 빨간 사탕이 왼쪽에 있음.
            if arr[0][0][1] == arr[1][0][1]:    # right
                arr[1][0][1] -= 1
            if arr[0][1][1] == arr[1][1][1]:    # left
                arr[0][1][1] += 1
    # up, down
    if blue_c == red_c:
        if blue_r < red_r:                  # 빨간 사탕이 아래 있음.
            if arr[1][2][0] == arr[0][2][0]:    # up
                arr[1][2][0] += 1
            if arr[0][3][0] == arr[1][3][0]:    # down
                arr[0][3][0] -= 1
        else:                               # 빨간 사탕이 위에 있음.
            if arr[1][2][0] == arr[0][2][0]:    # up
                arr[0][2][0] += 1
            if arr[0][3][0] == arr[1][3][0]:    # down
                arr[1][3][0] -= 1
    return arr


def pm(blue_r, blue_c, red_r, red_c):
    print('~' * N)
    for r in range(N):
        for c in range(M):
            if r == blue_r and c == blue_c:
                print('B', end = '')
            elif r == red_r and c == red_c:
                print('R', end = '')
            else:
                print(maze[r][c], end = '')
        print()
    return


def solve(blue_r, blue_c, red_r, red_c):
    # shape : N X M X N X M
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[blue_r][blue_c][red_r][red_c] = 1
    q = deque([(blue_r, blue_c, red_r, red_c)])
    while q:
        blue_r, blue_c, red_r, red_c = q.popleft()
        cur_depth = visited[blue_r][blue_c][red_r][red_c]
        # 깊이가 10인 경우에는 더 탐색하지 않는다.
        if cur_depth == 11:
            continue
        neigh = get_neigh(blue_r, blue_c, red_r, red_c)
        # print('_' * M)
        # print('iteration')
        # print(cur_depth)
        # pm(blue_r, blue_c, red_r, red_c)
        if neigh is None:
            return cur_depth
        else:
            blue_coords, red_coords = neigh
            for i in range(4):
                blue_coord = blue_coords[i]
                red_coord = red_coords[i]
                if blue_coord[0] is not None:
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
print(solve(blue_r, blue_c, red_r, red_c))
