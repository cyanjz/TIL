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
