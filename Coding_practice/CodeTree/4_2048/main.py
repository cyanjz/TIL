# tilt_left
def tilt(row):
    cursor = 0
    prev, cur = None, None
    new_row = [0] * N
    top = -1
    while cursor < N:
        # 새로운 요소를 발견하면 prev update
        if row[cursor] != 0:
            prev = cur
            cur = row[cursor]
            # 요소 비교
            if prev:
                # 같으면 prev * 2를 push하되, prev와 cur 둘다 None으로 초기화
                if prev == cur:
                    top += 1
                    new_row[top] = cur * 2
                    prev = None
                    cur = None
                # 다르면 prev push
                else:
                    top += 1
                    new_row[top] = prev
        cursor += 1
    if cur:
        top += 1
        new_row[top] = cur
    return new_row


def tilt_left(arr):
    for r in range(N):
        arr[r] = tilt(arr[r])


def tilt_right(arr):
    for r in range(N):
        arr[r] = tilt(arr[r][::-1])[::-1]


def tilt_up(arr):
    for c in range(N):
        col = tilt([arr[i][c] for i in range(N)])
        for r in range(N):
            arr[r][c] = col[r]


def tilt_down(arr):
    for c in range(N):
        col = tilt([arr[i][c] for i in range(N-1, -1, -1)])
        for r in range(N):
            arr[r][c] = col[N-1-r]


def solve_dfs_recursive(depth):
    global arr_3d, ans
    # visited의 dimension은? -> 생각 안나니까 일단 Depth 이용해서 재귀 돌려보기.
    # arr_3d에서 값들을 업데이트하기를 반복!
    if depth == 5:
        local_max = max([max(row) for row in arr_3d[depth]])
        ans = max(local_max, ans)
    else:
        for t in tilts:
            temp = [row[:] for row in arr_3d[depth]]
            t(temp)
            arr_3d[depth+1] = temp
            solve_dfs_recursive(depth+1)


tilts = [tilt_left, tilt_right, tilt_down, tilt_up]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_3d = [arr] + [[[0] * N for _ in range(N)] for _ in range(5)]
ans = 0
solve_dfs_recursive(0)
print(ans)
