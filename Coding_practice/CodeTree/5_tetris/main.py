import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# rotate 90%
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


def solve():
    global ans
    for r in range(N):
        for c in range(M):
            for i in range(5):
                # 1. 뒤집기 대칭 + 회전 대칭 -> 회전과 뒤집기 수행할 필요 없다.
                # 그냥 dr, dc 순회하면서 계산하기
                if mirror_symmetry[i] and rotation_symmetry[i]:
                    loc_sum = 0
                    for dr, dc in blocks[i]:
                        cr, cc = r + dr, c + dc
                        if 0 <= cr < N and 0 <= cc < M:
                            break
                        loc_sum += arr[cr][cc]
                    else:
                        ans = max(loc_sum, ans)
                # 2. 뒤집기 대칭 -> 뒤집을 필요 없고 회전만 수행한다.

    return


def is_dup(block1, block2):
    dup_count = 0
    # 16번 loop
    for i in range(len(block1)):
        for j in range(len(block2)):
            if block1[i] == block2[j]:
                dup_count += 1
    # 블록이 정확히 같은 경우에 False return
    if dup_count == len(block1):
        return True
    return False


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


# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 길쭉이, 네모, ㄱ자, 번개, ㅏ
temp = [((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1)),
        ((0, 0), (1, 0), (1, 1), (2, 1)),
        ((0, 0), (1, 0), (1, 1), (2, 0))]

# test = []
# a = temp[3][:]
# for i in range(4):
#     a = [rotate(r, c) for r, c in a]
#     test.append(a)
# print_blocks(test)


# build block
top = -1
blocks = [None] * 5
for original_block in temp:                  # block들을 불러오면서
    dump = list()                            # 특정 블록의 가능한 모든 case 저장할 임시 변수
    # original block rotation
    rotated_block = original_block[:]
    dump.append(rotated_block)
    for _ in range(3):                       # 돌리기
        rotated_block = [rotate(r, c) for r, c in rotated_block]
        for b in dump:
            if is_dup(rotated_block, b):
                break
        else:
            dump.append(rotated_block)

    # mirror block rotation
    mirror_rotated_block = [mirror(r, c) for r, c in original_block]
    for _ in range(4):
        mirror_rotated_block = [rotate(r, c) for r, c in mirror_rotated_block]
        for b in dump:
            if is_dup(mirror_rotated_block, b):
                break
        else:
            dump.append(mirror_rotated_block)
    top += 1
    blocks[top] = dump


# solve part



# mirror_symmetry = [True, True, False, False, False]
# rotation_symmetry = [False, True, False, False, False]
# solve()
