# Dijkstra
## 개요
가중치를 가지는 방향 그래프에서 특정 정점으로부터 다른 정점으로 가는 최단 거리를 계산하는 알고리즘.

greedy와 bfs를 합친 방식으로 이해하면 쉬우며 
<a href='../../Data Structure/Tree/MST/2_prim.md'>prim</a>
알고리즘과 유사하다.

의사 코드
```sudo
1. 초기화
    1) D 배열
    - 시작 정점과 다른 정점 사이의 최단 거리를 저장할 D 배열을 INF값으로 초기화 한다.
    - D 배열의 시작 정점 값을 0으로 할당한다.
    2) pq 우선순위 큐
    - 우선순위 큐를 (0, 시작 정점)로 초기화한다.
2. dijkstra
    1) 특정 노드의 최단 거리와 해당 노드를 pq에서 pop 한다.
    2) D[node] < distance일 경우 이미 다른 경로를 통해서 탐색을 진행했기 때문에 더 이상 탐색하지 않는다.
    3) node의 모든 인접한 next_node에 대하여
        1] D[next_node] <= D[node] + next_weight 인 경우에는 continue.
            더 작은 경로가 존재하는데 next_node를 탐색할 이유가 없다.
        2] D[next_node] 를 D[node] + next_weight로 설정한다.
        3] pq에 (D[node] + next_weight, next_node)를 push한다.
```


## 구현 - python

```python
import heapq
import sys

sys.stdin = open('dijkstra_graph.txt', 'r')


def dijkstra(start):
    q = [(0, start)]
    D = [float('inf')] * V
    D[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if D[node] < cost:
            continue
        for n_w, next_node in adj_list[node]:
            next_cost = n_w + D[node]
            if D[next_node] <= next_cost:
                continue
            D[next_node] = next_cost
            heapq.heappush(q, (next_cost, next_node))
    return D


V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj_list[s].append((w, e))
print(dijkstra(0))
```