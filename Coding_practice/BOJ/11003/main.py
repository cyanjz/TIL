# deque에 하나씩 넣고
# 최솟값 업데이트?
# 최악의 경우 5000000**2 = 25,000,000,000,000 (불가능)
# 그럼 seg tree를 사용? -> O(NlogN) ~ 111,267,483 (가능)
# 276,000,000 (제한)
# seg tree를 만드는 것은 어떤가? -> 160 MB 가능함.


def build_tree(left, right, node):
    if left == right:
        st[node] = a_list[left]
    else:
        mid = (left+right)//2
        build_tree(left, mid, 2*node)
        build_tree(mid+1, right, 2*node+1)
        st[node] = min(st[2*node], st[2*node+1])


def quarry_tree(left, right, node, start, end):
    if left >= start and right <= end:
        return st[node]
    elif left > end or right < start:
        return 1000000000
    else:
        mid = (left+right)//2
        left_value = quarry_tree(left, mid, 2*node, start, end)
        right_value = quarry_tree(mid+1, right, 2*node+1, start, end)
        return min(left_value, right_value)


def solve():
    build_tree(0, N-1, 1)
    ds = [0] * N
    for i in range(N):
        ds[i] = quarry_tree(0, N-1, 1, max(0, i-L+1), i)
    print(*ds)


st = [0] * 20000000
N, L = map(int, input().split())
a_list = list(map(int, input().split()))
solve()
