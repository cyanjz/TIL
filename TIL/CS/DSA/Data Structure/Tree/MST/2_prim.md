# prim
## 개요
prim은 MST에 정점을 하나씩 추가하면서 MST를 완성하는 방식의 알고리즘이다.

MST의 노드와 인접한 정점과의 간선 중에서 가중치가 가장 낮은 것을 선택하여 해당 정점이 MST에 포함되지 않은 정점일 경우에 MST에 추가하는 과정을 반복한다.

이때 우선 순위 큐, heap을 사용하면 정점의 추가와 삭제가 $\log{n}$의 시간 복잡도를 가지기 때문에 구현상의 이점이 있다. 그러나 prim 알고리즘이 무조건 heap을 사용해야하는 알고리즘이 아님에 유의한다.

MST가 완성되는 조건 : V개의 정점을 모두 선택한 경우이므로 cnt 변수를 사용하여 V만큼의 정점이 MST에 포함되면 루프를 종료.

## 구현 - Python
prim을 사용하여 MST를 구현하는 방식은 여러가지 방식이 있다.

heapq를 무조건적으로 사용해야하는 것은 아님에 유의한다.

### 1. 기본적인 prim 알고리즘 (prim1)
이 경우에는 MST에 포함된 노드인지 여부를 확인하여 포함된 노드인 경우에는 비록 우선순위 큐에 포함된 최소의 간선일지라도 포함시켜선 안된다.(cycle이 형성되기 때문.)

따라서 MST 포함 여부를 확인하는 MST 배열을 만들어 관리해준다.

### 2. 개선된 prim 알고리즘 (prim2)
기본적인 prim 알고리즘에 더해 지금 MST에서 특정 node로 가는 최소 가중치를 추적하면서, 해당 node로 가는 다른 방법이 발견되어도 특정 node로 가는 가중치가 더 크다면 heap에 추가하지 않는다.


```python
import heapq
import sys

sys.stdin = open('tree.txt', 'r')


# without optimization
def prim1():
    pq = list()
    pq.append((0, 0))
    MST = [0] * V
    min_cost = 0
    cnt = 0
    while cnt < V:
        cost, node = heapq.heappop(pq)
        if MST[node] == 1:
            continue
        MST[node] = 1
        min_cost += cost
        cnt += 1
        for weight, next_node in adj_list[node]:
            if MST[next_node]:
                continue
            heapq.heappush(pq, (weight, next_node))
    return min_cost


# with optimization
def prim2():
    pq = list()
    pq.append((0, 0))
    MST = [0] * V
    keys = [float('inf')] * V                   # MST에서 node를 잇는 최단거리.
    min_cost = 0
    cnt = 0
    while pq and cnt < V:
        cost, node = heapq.heappop(pq)
        if MST[node]:
            continue
        MST[node] = 1
        min_cost += cost
        for next_cost, next_node in adj_list[node]:
            # 조건 하나 더 추가 -> 이미 최단 거리
            if MST[next_node] or keys[next_node] <= next_cost:
                continue
            keys[next_node] = next_cost
            heapq.heappush(pq, (next_cost, next_node))
    return min_cost


V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj_list[s].append((w, e))
    adj_list[e].append((w, s))
print(prim2())

```