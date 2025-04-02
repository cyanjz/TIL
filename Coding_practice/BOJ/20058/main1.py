from collections import deque


def rotate_all(l):
    # 봐야할 scope는 0~2**(L+1).
    # 근데 l==N이면 안됨.
    if l == N:
        return
    else:
        # 시작 위치는... (0, 0), (2**(l+1), 0), ... (2**(N-l), 0) () 2**(l+1)만큼 stride.
        stride = 2**(l+1)
        for r in range(0, arr_size, stride):
            for c in range(0, arr_size, stride):
                rotate_local(r, c, l)
        return


def rotate_local(r, c, l):
    size = 2**l
    # 나중에 불러오기 위한 변수.
    # temp = [row[c:c+size] for row in arr[r:r+size]]

    # A | B
    # D | C
    # A : r + i,        c + j
    # B : r + i,        c + size + j
    # C : r + i + size, c + size + j
    # D : r + i + size, c + j
    for i in range(size):
        for j in range(size):
            cr, cc = r + i, c + j
            # A B C D = D A B C
            arr[cr][cc], arr[cr][cc+size], arr[cr+size][cc+size], arr[cr+size][cc] = arr[cr+size][cc], arr[cr][cc], arr[cr][cc+size], arr[cr+size][cc+size]
    # print('#' * arr_size)
    # for row in arr:
    #     print(*row)
    return


def melt():
    does_melt = [[0] * arr_size for _ in range(arr_size)]
    for r in range(arr_size):
        for c in range(arr_size):
            num_ice = 0
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                if 0 <= nr < arr_size and 0 <= nc < arr_size and arr[nr][nc]:
                    num_ice += 1
            if num_ice < 3:
                does_melt[r][c] = 1
    for r in range(arr_size):
        for c in range(arr_size):
            arr[r][c] -= does_melt[r][c]
    # print('#' * arr_size)
    # for row in arr:
    #     print(*row)
    return


def get_max_chunk():
    visited = [[0] * arr_size for _ in range(arr_size)]
    max_chunk_size = 0
    for r in range(arr_size):
        for c in range(arr_size):
            if visited[r][c] or arr[r][c] == 0:
                continue
            q = deque()
            q.append((r, c))
            visited[r][c] = 1
            chunk_size = 0
            while q:
                cr, cc = q.popleft()
                chunk_size += 1
                for dr, dc in ds:
                    nr, nc = cr + dr, cc + dc
                    if visited[nr][nc] or arr[nr][nc] == 0:
                        continue
                    visited[nr][nc] = 1
                    q.append((nr, nc))
            max_chunk_size = max(chunk_size, max_chunk_size)
    return max_chunk_size


def solve():
    for l in Ls:
        rotate_all(l)
        melt()
    max_chunk_size = get_max_chunk()
    return max_chunk_size, sum(sum(row) for row in arr)


ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, Q = map(int, input().split())
arr_size = 2**N
arr = [list(map(int, input().split())) for _ in range(arr_size)]
Ls = list(map(int, input().split()))
max_chunk, total_ice = solve()
print(total_ice)
print(max_chunk)
