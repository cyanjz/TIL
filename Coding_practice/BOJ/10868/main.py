import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
input = sys.stdin.readline


def build_tree(left, right, node):
    global st
    if left == right:
        st[node] = arr[left]
    else:
        mid = (left+right)//2
        build_tree(left, mid, 2*node)
        build_tree(mid+1, right, 2*node+1)
        st[node] = min(st[2*node], st[2*node+1])


def query_tree(left, right, start, end, node):
    # 1. start, end가 벗어난 경우 선택되서는 안되므로 0을 반환.
    # else에서 선택될 수 없는 값을 반환하도록 해야한다.
    if end < left or start > right:
        return MAXV
    # 2. (left, right) in (start, end)
    # 해당 node의 값을 반환해서 부모 노드에서 비교할 수 있도록 하기.
    elif start <= left and right <= end:
        return st[node]
    # 3. 그 외의 경우. 즉, 반쯤 걸친 경우. 두 자식으로 쿼리를 보내고 최댓값을 반환.
    else:
        mid = (left+right)//2
        left_value = query_tree(left, mid, start, end, 2*node)
        right_value = query_tree(mid+1, right, start, end, 2*node+1)
        return min(left_value, right_value)


# read inputs
N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
# initialize tree variables
MAXV = 1000000000
st = [MAXV] * (4*N)                                                    # 4 * N is safe
build_tree(0, N-1, 1)
# read queries and return value
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    print(query_tree(0, N-1, a, b, 1))
