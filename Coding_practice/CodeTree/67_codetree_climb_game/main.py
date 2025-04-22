# 1. 필요한 자료구조
# 1) tree : segment tree. 각 height 별로 lis값을 가지고 있는 arr에 대한 seg tree
# 2) ans : 특정 index의 lis를 저장하고 있는 배열. stack.
# 3) mountains : 특정 index의 산의 높이를 저장하고 있는 배열. stack.
# 4) backup-arr : 특정 index의 산이 삭제될 경우를 대비하여 존재하는 stack. list of lis.

# 2. 알고리즘
# 1) add_mountain
#   1> mountains에 새로운 산을 업데이트
#   2> tree의 height값을 갱신
#   3> ans에 새로 들어온 index의 lis 값 갱신하기.
# 2) earth_quake
#   1> mountains pop 수행
#   2> ans pop 수행
#   3> ans의 마지막 요소 -> (idx, lis - 1) 해당 index의 이전 lis를 기반으로 tree를 업데이트 해줘야함.
#       1] ans에 저장될 값들은, 해당 height가 추가되기 이전의 lis 값을 저장.
import sys
sys.stdin = open("edge.txt", 'r')
sys.stdout = open('output.txt', 'w')


QMAX = 500000
HMAX = 1000000
st = [[0, 0] for _ in range(HMAX*4+1)]                          # (height, lis)
top = -1
mountains = [0] * (QMAX * 2)
ans = [0] * (QMAX * 2)
backup_arr = [0] * (QMAX * 2)


def update_tree(left, right, node, value):
    global st, top, mountains, ans
    if value[0] < left or value[0] > right:
        return
    if left == right:
        st[node] = value
    else:
        mid = (left+right) // 2
        update_tree(left, mid, 2*node, value)
        update_tree(mid+1, right, 2*node+1, value)
        # 자식들의 lis 비교
        if st[2*node][1] < st[2*node+1][1]:
            st[node] = st[2*node+1]
        elif st[2*node+1][1] < st[2*node][1]:
            st[node] = st[2*node]
        # 자식들의 lis가 동일한 경우에는 height 비교
        else:
            if st[2*node][0] < st[2*node+1][0]:
                st[node] = st[2*node+1]
            else:
                st[node] = st[2*node]


def query_tree(left, right, start, end, node):
    # left, right -> 현재 노드가 참조하는 배열의 범위
    # start, end -> query의 배열의 범위
    global st, top, mountains, ans
    if right < start or end < left:
        return [0, 0]
    if start <= left and right <= end:
        return st[node]
    mid = (left+right) // 2
    left_value = query_tree(left, mid, start, end, 2 * node)
    right_value = query_tree(mid+1, right, start, end, 2 * node+1)
    if left_value[1] < right_value[1]:
        return right_value
    elif left_value[1] > right_value[1]:
        return left_value
    else:
        if left_value[0] < right_value[0]:
            return right_value
        else:
            return left_value


# 100
def bigbang(args):
    for i in range(len(args)):
        add_mountain(args[i])
        # print(*st)
    return


# 200
# 1) add_mountain
#   1> mountains에 새로운 산을 업데이트
#   2> tree의 height값을 갱신 -> query를 날려서 해당 높이보다 1 낮은 산의 lis를 구하기.
#   3> ans에 새로 들어온 index의 lis 값 갱신하기.
def add_mountain(height):
    global st, top, mountains, ans
    # segtree update
    top += 1
    mountains[top] = height
    temp_height, temp_lis = query_tree(1, HMAX, 1, height-1, 1)
    backup_height, backup_lis = query_tree(1, HMAX, height, height, 1)
    # print('__________add mountain called__________')
    # print(f'height : {height}, temp_height : {temp_height}, temp_lis : {temp_lis}')
    # print(f'backup_height : {backup_height}, backup_lis : {backup_lis}')
    backup_arr[top] = backup_lis
    ans[top] = temp_lis + 1
    update_tree(1, HMAX, 1, [height, temp_lis+1])
    return


# 300
# 2) earth_quake
#   1> mountains pop 수행
#   2> ans pop 수행
#   3> ans의 마지막 요소 -> (idx, lis - 1) 해당 index의 이전 lis를 기반으로 tree를 업데이트 해줘야함.
#       1] ans에 저장될 값들은, 해당 height가 추가되기 이전의 lis 값을 저장.
def earthquake():
    global st, top, mountains, ans
    del_height = mountains[top]
    del_lis = backup_arr[top]
    # print('__________earthquake called__________')
    # print(f'del_height : {del_height}, del_lis : {del_lis}')
    update_tree(1, HMAX, 1, [del_height, del_lis])
    top -= 1
    return


# 400
def climb_simulation(m_index):
    max_lis_height, max_lis = query_tree(1, HMAX, 1, HMAX, 1)
    m_index_lis = ans[m_index]
    print('climb_called')
    print(m_index-1)
    # print(*ans[:top+1])
    # print(*mountains[:top+1])
    print(max_lis_height, max_lis, m_index_lis)
    print((max_lis-1 + m_index_lis-1 + 1) * 1000000 + max_lis_height)


Q = int(input())
for q in range(Q):
    cmd, *args = map(int, input().split())
    if cmd == 100:
        bigbang(args)
    elif cmd == 200:
        add_mountain(*args)
    elif cmd == 300:
        earthquake()
    else:
        climb_simulation(*args)
    # print(f'{q}_______________________________________')
    # print(st)
    # print(mountains[:top+1])
    # print(ans[:top+1])
