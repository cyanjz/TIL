import sys

sys.stdin = open('tree.txt', 'r')


def make_set():
    return [i for i in range(V)]


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x_ref, y_ref = find_set(x), find_set(y)
    if x_ref == y_ref:
        return False
    elif x_ref > y_ref:
        parents[x_ref] = y_ref
    else:
        parents[y_ref] = x_ref
    return True


def kruskal():
    top = -1
    min_cost = 0
    cnt = 0
    while cnt < V-1:
        top += 1
        s, e, w = edges[top]
        if union(s, e):
            cnt += 1
            min_cost += w
    return min_cost


# read input & sort edges
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
# initialize set
parents = make_set()
# run kruskal
print(kruskal())
