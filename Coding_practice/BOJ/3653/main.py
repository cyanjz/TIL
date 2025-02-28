# pyhton index method O(n * m) -> 1E8. not available.
def solve1():
    ans = [0] * m
    top = -1
    for target in targets:
        idx = movies.index(target)
        num = movies.pop(idx)
        movies.append(num)
        top += 1
        ans[top] = n-idx-1
    return ans


# build segtree
def build_tree(node, left, right):
    global tree_index
    if left == right:
        st[node] = arr[left]
    else:
        mid = (left+right)//2
        build_tree(2 * node, left, mid)               # left child
        build_tree(2 * node + 1, mid+1, right)        # right child
        st[node] = st[2*node] + st[2*node+1]


def update_tree(node, arr_idx, val, left, right):
    global st, arr
    if left == right:
        st[node] = val
        try:
            arr[arr_idx] = val
        except:
            breakpoint()
    else:
        mid = (left+right)//2
        if left <= arr_idx <= mid:                      # index in left
            update_tree(2*node, arr_idx, val, left, mid)
        else:                                           # index in right
            update_tree(2*node+1, arr_idx, val, mid+1, right)
        st[node] = st[2*node] + st[2*node+1]


def query_tree(node, qs, qe, l, r):
    if qe < l or r < qs:                                # out range
        return 0
    if qs <= l and r <= qe:                             # in range
        return st[node]
    else:                                               # semi in range
        mid = (l+r)//2
        return query_tree(2*node+1, qs, qe, mid+1, r) + query_tree(2*node, qs, qe, l, mid)


def query_update_tree(node):
    global tree_top, st
    height = 0
    result = 0
    tree_top += 1                                      # add 1 to tree_top so always put element to the top
    while node != 1:                                   # while not root node
        st[node] = tree_top                            # update value to tree_top
        parent_node = node // 2                        # index of parent node
        if st[parent_node] > st[node]:                 # check whether a parent is larger or not
            break
        result += 2 ** height
        height += 1
        node = parent_node
    print(result)
    return result


T = int(input())
st = [0] * 800000                                     # segment tree size = upper bound of (n+m)*4
tree_index = [0] * 100001                             # book index -> tree index
for t in range(T):
    n, m = map(int, input().split())                  # read input
    targets = list(map(int, input().split()))         # size : m
    movies = [0] + [(n-i-1) for i in range(n)]          # size : n movie_num -> arr_idx
    # print(movies)
    arr = [1] * n + [0] * m
    top = n - 1                                       # value for updating nodes in each iteration.
    ans = [0] * m
    # print(*st[:tree_size+1])
    build_tree(1, 0, n+m-1)                           # build st
    # print(*st[:20])
    for i, target in enumerate(targets):              # for target in targets
        # query tree
        # print(st[:n*m])
        # print(movies[target]+1)
        # print(top)
        # print(*arr)
        ans[i] = query_tree(1, movies[target]+1, top, 0, n+m-1)
        # update tree
        update_tree(1, movies[target], 0, 0, n+m-1)                # update tree
        top += 1
        update_tree(1, top, 1, 0, n+m-1)                      # update tree
        movies[target] = top
        # ans[i] = query_update_tree(tree_index[target])
    print(*ans)
