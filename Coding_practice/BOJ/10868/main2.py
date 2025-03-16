import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n,m = map(int,input().split())

tree_height = 0
length = n

while length != 0:
    length //= 2
    tree_height += 1

tree_size = pow(2, tree_height + 1)

left_node_start_index = (tree_size // 2) - 1
tree = [sys.maxsize] * (tree_size+1)

for i in range(left_node_start_index+1,left_node_start_index+n+1):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        if tree[i//2] > tree[i]:
            tree[i//2] = tree[i]
        i -= 1

def get_sum(s,e):
    part_sum = sys.maxsize
    # 탐색종료 조건
    while s <= e:
        if s % 2 == 1:
            part_sum = min(tree[s],part_sum)
            s += 1
        if e % 2 == 0:
            part_sum = min(tree[e],part_sum)
            e -= 1
        # 부모 노드로 이동
        s = s//2
        e = e//2
    return part_sum

set_tree(tree_size-1) #초기 트리 생성

print(tree[:tree_size])

for _ in range(m):
    s, e = map(int,input().split())
    s = s + left_node_start_index
    e = e + left_node_start_index
    print(get_sum(s,e))