# 1. make set
def make_set(num_sets):
    p = [i for i in range(num_sets+1)]
    r = [0 for i in range(num_sets+1)]
    return p, r


# 2.find set
def find_set_iteration(x):
    while x != parents[x]:
        # move cursor to its parent
        parents[x] = parents[parents[x]]
        # compression
        x = parents[x]
    return x


def find_set_recursive(x):
    if x == parents[x]:
        return x
    parents[x] = find_set_recursive(parents[x])
    return parents[x]


# 3. union set
def union(x, y):
    x_ref = find_set_recursive(x)
    y_ref = find_set_recursive(y)
    # case1. x_ref < y_ref
    # x_ref가 y_ref보다 작기 때문에 x_ref에 y_ref를 붙여줘야함.
    # 즉, y_ref의 parent를 x_ref로 업데이트.
    # case2. x_ref > y_ref
    # x_ref의 parent를 y_ref로 업데이트
    if x_ref < y_ref:
        parents[y_ref] = x_ref
    elif x_ref > y_ref:
        parents[x_ref] = y_ref


def union_rank(x, y):
    x_ref = find_set_recursive(x)
    y_ref = find_set_recursive(y)
    x_ref_rank = ranks[x_ref]
    y_ref_rank = ranks[y_ref]
    if x_ref_rank < y_ref_rank:
        parents[x_ref] = y_ref
    elif x_ref_rank > y_ref_rank:
        parents[y_ref] = x_ref
    else:
        parents[x_ref] = y_ref
        ranks[y_ref] += 1



parents, ranks = make_set(10)
