from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def solve():
    stack = deque()
    stack.extend([node for node in range(V) if inorder[node] == 0])
    depths = [0 if inorder[node] else 1 for node in range(V)]
    while stack:
        cur_node = stack.pop()
        for next_node in adj_list[cur_node]:
            inorder[next_node] -= 1
            depths[next_node] = max(depths[next_node], depths[cur_node] + 1)
            if inorder[next_node] == 0:
                stack.append(next_node)
    return max(depths)


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    edges = map(int, input().split())
    adj_list = [[] for _ in range(V)]
    inorder = [0] * V
    for i in range(E):
        s, e = edges.__next__()-1, edges.__next__()-1
        inorder[e] += 1
        adj_list[s].append(e)
    print(f'#{t+1}', solve())
