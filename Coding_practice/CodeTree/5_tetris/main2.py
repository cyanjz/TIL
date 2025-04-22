# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


# to make ds
def rotate(r, c):
    # 2, 1 (down) -> 1, -2 (left)
    # 1, -2 (left) -> -2, -1 (up)
    # -2, -1 (up) -> -1, 2 (right)
    # -1, 2 (right) -> 2, 1 (down)
    # row, col -> col, -row
    return c, -r


def mirror(r, c):
    # horizontal mirror coords ->
    # 2, 1 -> 2, -1
    return r, -c


# to check ds
def print_blocks(blocks):
    print('_' * 17)
    cr, cc = 4, 4
    for block in blocks:
        print('~' * 17)
        print_map = [[0] * 9 for _ in range(9)]
        for r, c in block:
            print_map[cr+r][cc+c] = 1
        for row in print_map:
            print(*row)
    return


def solve():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for r in range(N):
        for c in range(M):
            for d in ds:
                loc_sum = 0
                for dr, dc in d:
                    cr, cc = r + dr, c + dc
                    if 0 <= cr < N and 0 <= cc < M:
                        loc_sum += arr[cr][cc]
                    else:
                        break
                else:
                    max_sum = max(loc_sum, max_sum)
    return max_sum


# original blocks
temp = [((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1)),
        ((0, 0), (1, 0), (1, 1), (2, 1)),
        ((0, 0), (1, 0), (1, 1), (2, 0))]


# 1
linear = [[(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (2, 0), (3, 0)]]

# ㅁ
square = [[(0, 0), (0, 1), (1, 0), (1, 1)]]

# ㄱ
r_shape = []
original_r = [(0, 0), (1, 0), (2, 0), (2, 1)]
rotated_r = original_r[:]
for i in range(4):
    rotated_r = [tuple(rotate(r, c)) for r, c in rotated_r]
    m_rotated_r = [tuple(mirror(r, c)) for r, c in rotated_r]
    r_shape.append(rotated_r)
    r_shape.append(m_rotated_r)

# 번개
l_shape = []
lightening = temp[3]
m_l = [tuple(mirror(r, c)) for r, c in lightening]
rotated_l = [tuple(rotate(r, c)) for r, c in lightening]
m_rotated_l = [tuple(mirror(r, c)) for r, c in rotated_l]
l_shape.append(lightening)
l_shape.append(m_l)
l_shape.append(rotated_l)
l_shape.append(m_rotated_l)

# ㅏ
k_shape = []
rotated_k = temp[-1]
for i in range(4):
    rotated_k = [tuple(rotate(r, c)) for r, c in rotated_k]
    k_shape.append(rotated_k)


ds = [*linear, *square, *r_shape, *l_shape, *k_shape]


print(solve())

# for d in ds:
#     print_blocks(d)
