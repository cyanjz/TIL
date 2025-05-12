from collections import deque


def tp_sort():
    ans = [0] * N
    for root in roots:
        ans[root] = cost_list[root]
    q = deque(roots)
    while q:
        # print(q)
        # print(ans)
        node = q.popleft()
        for adj_node in adj_mat[node]:
            # 인접한 노드에 대해서 counts - 1 하기
            counts[adj_node] -= 1
            # counts가 0이 될 경우 push
            if counts[adj_node] == 0:
                q.append(adj_node)
            # push와 무관하게 ans 배열 업데이트.
            ans[adj_node] = max(ans[adj_node], ans[node]+cost_list[adj_node])
    return ans
            

N = int(input())
adj_mat = [[] for _ in range(N)]
cost_list = [0] * N
counts = [0] * N
roots = []
for node in range(N):
    cost, *args = map(int, input().split())
    cost_list[node] = cost
    i = 0
    if args[i] == -1:
        roots.append(node)
        continue
    while args[i] != -1:
        adj_node = args[i]
        adj_mat[adj_node-1].append(node)
        i += 1
    counts[node] = i
# print(adj_mat)
# print(cost_list)
# print(*counts)
# print(*tp_sort())
for cost in tp_sort():
    print(cost)