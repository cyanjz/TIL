import heapq
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def solve(t):
    q = []
    Ds = [float('inf')] * N
    Ds[S] = 0
    visited = [0] * N
    visited[S] = 1
    for next_node, weight in adj_mat[S]:
        heapq.heappush(q, (weight+t, next_node))
    while q:
        cost, node = heapq.heappop(q)
        if visited[node]:
            continue
        visited[node] = 1
        Ds[node] = cost
        if node == D:
            break
        for next_node, weight in adj_mat[node]:
            heapq.heappush(q, (weight + cost + tax, next_node))
        # for next_node, weight in adj_mat[node]:
        #     next_cost = cost + weight + t
        #     if visited[next_node]:
        #         continue
        #     Ds[next_node] = next_cost
        #     visited[next_node] = 1
        #     heapq.heappush(q, (next_cost, next_node))
    return Ds[D]


N, M, K = map(int, input().split())
# 시작, 끝
S, D = map(lambda x: int(x)-1, input().split())
adj_mat = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    adj_mat[a].append((b, w))
    adj_mat[b].append((a, w))
# dijkstra 30000번? 에반데...
# 그럼 어떻게 해야할까
# 음... 한번의 dijkstra에서 모든 세금에 대한 연산을 수행하기.
# 별 차이 없을텐데? -> 이거 어차피 노드 방문 수가 1000번으로 고정되어 있으니까
# 대충 계산하면 될듯.
# 안되네... 그럼 tax별로 업데이트가 정해져 있으니까
#

tax = 0
print(solve(tax))
for k in range(K):
    tax += int(input())
    print(solve(tax))
