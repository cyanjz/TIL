# Kruskal
## 개요
kruskal 알고리즘은 가장 짧은 간선을 추가하면서 MST를 찾아가는 알고리즘이다.

간선 배열을 가중치를 기준으로 정렬하면 가장 짧은 간선부터 순서대로 MST에 추가할 수 있다.

그러나 cycle이 생기는 경우를 유의해야 한다.

가장 짧은 간선을 반복적으로 추가하는 것은 cycle이 생기는 것을 방지할 수 없다.

따라서 disjoint set을 사용하여 이미 edge의 두 정점이 같은 집합에 속한다면 union을 수행하지 않는 방식으로 해결할 수 있다.

## 구현 - python
정렬된 edges list에서 순차적으로 start, end, weight를 뽑아서 union을 시도한다.

union이 이루어질 경우에는 cnt(선택한 간선의 수)를 1 증가시키고 min_cost(MST total cost)에 weight를 더한다.

간선의 수가 V-1이 되면 종료한다.


```python
import sys

sys.stdin = open('tree.txt', 'r')


# make_set
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


# kruskal algorithm
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
```