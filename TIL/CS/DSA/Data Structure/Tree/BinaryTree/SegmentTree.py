# 일반적으로 길이가 배열에서 N인 구간의 합을 구하려면 O(N)의 시간 복잡도를 가진다.
# 그러나 Segment tree를 사용하면 O(logN)으로 줄일 수 있다.
# 구간 합을 많이 구해야 하는 경우에 segment tree를 사용하자!
#
# 구현에서 생각해야할 부분
# 0. 초기화 -> 4 * N으로 초기화.
# 1. Segment tree builder -> list를 바탕으로 만들기. -> recursion을 사용.
#     - node's left child index = 2 * node. node's right child index = 2 * node + 1
# 2. update -> 특정 값이 수정되었을 경우에 segment tree를 업데이트.
#   - node update. 그러니까.. 특정 idx의 값을 업데이트 했을 때 segment tree에 어떻게 반영을 할 것 인지?
#   - 재귀적으로 호출. idx가 왼쪽에 있는 값인지 오른쪽에 있는 값인지 확인하면서 tree를 재귀적으로 탐색하고
#       업데이트된 것을 기반으로 현재 node를 업데이트.
# 3. query -> 특정 범위의 합을 구하는 방법.
#   - 1. query의 scope를 고려하면서 scope 내에 현재 보고 있는 node의 범위가 들어가면, 즉 node가 query의 부분 집합
#       에 해당하면 node값을 더하기
#   - 2. 벗어나면 바로 return
#   - 3. query에 node의 범위가 걸치면... 왼쪽과 오른쪽 자식을 재귀적으로 탐색.
#   - scope 범위가 query에 포함(st[node])/벗어남(0)/걸침(q(left)+q(right) 에 대한 코드 작성.
#
# 중요! : segment tree를 형성할 때 최대값 혹은 최솟값으로 설정하여 tree를 만들 수도 있다.
# 구간에 대한 어떤 정보를 저장해 두는 형식으로 응용할 수 있음을 항상 생각하라!


def builder(node, left, right):
    global seg_tree
    if left == right:
        seg_tree[node] = arr[left]
    else:
        mid = (left+right)//2
        builder(2 * node, left, mid)  # left child update
        builder(2 * node+1, mid+1, right)  # right child update
        seg_tree[node] = seg_tree[2*node] + seg_tree[2*node+1]


def update(node, left, right, val, idx):
    global seg_tree
    if left == right:
        seg_tree[node] += val
    else:
        mid = (left+right)//2
        if left <= idx <= mid:
            update(2 * node, left, mid, val, idx)
        else:
            update(2 * node+1, mid+1, right, val, idx)
        seg_tree[node] = seg_tree[2*node] + seg_tree[2*node+1]


def query(node, s, e, left=0, right=6):
    # s, e -> query
    # l, r -> scope
    # query가 scope를 벗어나는 경우.
    if e < left or right < s:
        return 0
    # scope가 querry 내에 있는 경우.
    if s <= left and right <= e:
        return seg_tree[node]
    mid = (left+right)//2
    return query(2*node, s, e, left, mid) + query(2*node+1, s, e, mid+1, right)


arr = [1, 2, 3, 4, 5]
N = len(arr)
seg_tree = [0] * (2 * N)
builder(1, 0, N-1)
# update(1, 0, N-1, 100, 1)
print(seg_tree)
# update(1, 0, N-1, 100, 4)
# print(seg_tree)
