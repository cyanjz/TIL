def build_ST(node, l, r):
    if l == r:
        ST[node] = arr[l]
    else:
        mid = (l+r)//2
        build_ST(2*node, l, mid)
        build_ST(2*node+1, mid+1, r)
        ST[node] = ST[2*node] + ST[2*node+1]


def update(node, idx, val, l, r):
    if l == r:
        ST[node] = val
        return
    mid = (l+r)//2
    if idx <= mid:
        update(2*node, idx, val, l, mid)
    else:
        update(2*node+1, idx, val, mid+1, r)
    ST[node] = ST[2*node] + ST[2*node+1]


def query(node, s, e, l, r):
    if e < l or r < s:
        return 0
    if s <= l and r <= e:
        return ST[node]
    mid = (l+r)//2
    return query(2*node, s, e, l, mid) + query(2*node+1, s, e, mid+1, r)


N, M, K = map(int, input().split())  # arr 크기, 변경 횟수, 구간합 횟수
ST = [0] * (4 * N)
arr = [int(input()) for _ in range(N)]
build_ST(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, b-1, c, 0, N-1)
    else:
        print(query(1, b-1, c-1, 0, N-1))
