import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def gcd(a, b):
    # a > b
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def traverse_graph(root, ans):
    node = root
    visited = [0] * N
    while node == root or inorder[node] == 2:
        print(node)
        visited[node] = 1
        for next_node, p, q in adj_mat[node]:
            if visited[next_node]:
                continue
            ans[next_node] = ans[node] * p // q
            node = next_node
    print(ans)
    return

# end condition : depth == N-1 or cnt == 2
# pruning : N-1 - depth < 2 - cnt
def solve(root):
    ans = [0] * N
    upper = 1
    lower = 1
    node = root[0]
    visited = [0] * N
    # bfs로 수정하기.
    # 그냥 null space 구하는게 좋을 듯
    while node == root[0] or inorder[node] == 2:
        print(node)
        visited[node] = 1
        # a/b = p/q
        # q * a = p * b
        # a = p/q * b
        for next_node, p, q in adj_mat[node]:
            if visited[next_node]:
                continue
            upper *= p
            lower += q
            node = next_node
    if upper > lower:
        # root[0] = upper / lower * root[1]
        # root[1] = gcd
        greatest_common = gcd(upper, lower)
        ans[root[1]] = greatest_common
        node = root[1]
        traverse_graph(node, ans)
    else:
        # root[1] = lower / upper * root[0]
        # root[0] = gcd
        greatest_common = gcd(lower, upper)
        ans[root[0]] = greatest_common
        node = root[0]
        traverse_graph(node, ans)
    return ans


N = int(input())
ratios = [list(map(int, input().split())) for _ in range(N-1)]
inorder = [0] * N
adj_mat = [[] for _ in range(N)]
for a, b, p, q in ratios:
    adj_mat[a].append((b, p, q))
    adj_mat[b].append((a, q, p))
    inorder[a] += 1
    inorder[b] += 1

print('###')
root = []
for i in range(N):
    if inorder[i] == 1:
        root.append(i)
print(*inorder)

print(gcd(36, 12))
# a / b  = p / q, a : b = p : q
# 가능한 모든 쌍에 대하여 최소 공배수 계산해서 곱해주기.
# 그러니까... 4를 이미 일정량 넣었다고 해도 다른 비율에서는 그만큼을 제외하고 다시 더 넣어줘야함.
# 그럼 각 비율을 별도로 관리하면서 조합 찾고 최소 공배수 찾아서 곱해주기.
# print(solve(0, 0, 1 << N-1))
print(solve(root))
