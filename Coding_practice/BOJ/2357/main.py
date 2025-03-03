import sys


def buildst(node, left, right):
    global ST
    if left == right:
        ST[node] = (arr[left], arr[right])
        return
    else:
        mid = (left+right)//2
        buildst(2*node, left, mid)
        buildst(2*node+1, mid+1, right)
        ST[node] = min(ST[2*node][0], ST[2*node+1][0]), max(ST[2*node][1], ST[2*node+1][1])
        return


def merge_resp(resp1, resp2):
    return min(resp1[0], resp2[0]), max(resp1[1], resp2[1])


def query(node, start, end, left, right):
    # start ~ end가 left ~ right 밖에 있음
    if end < left or right < start:
        return MAXV, MINV
    # left ~ right 가 start~end에 포함됨.
    if start <= left and right <= end:
        return ST[node]
    # 그외의 경우. 즉, 일부가 겹치는 경우.
    else:
        mid = (left+right)//2
        resp1 = query(2 * node, start, end, left, mid)
        resp2 = query(2 * node + 1, start, end, mid+1, right)
        return merge_resp(resp1, resp2)


MINV = 1
MAXV = 1000000000
N, M, *read = map(int, sys.stdin.read().split())
arr = read[:N]
qs = read[N:]
ST = [0] * (4*N)
buildst(1, 0, N-1)
for m in range(M):
    a, b = qs[2*m], qs[2*m+1]
    print(*query(1, a-1, b-1, 0, N-1))
