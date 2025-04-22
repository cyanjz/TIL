import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


# 정점이 주어졌을 때 해당 그래프에서 가장 많은 쌍을 만들고
# 쌍의 갯수를 반환하는 함수.
# 어... 음... 그냥 bf 돌리면 시간 복잡도가 비슷할텐데
# 그럼 짝수인 간선 수와 홀수인 간선 수를 세볼까?
def get_neigh(r, c):
    cur_w = defence_center[r][c]
    result = []
    for func in funcs:
        nr, nc = func((r, c))
        n_w = defence_center[nr][nc]
        if n_w + cur_w <= W:
            result.append((nr, nc))
    return result


def get_matching(e):
    global visited, twos
    for r in range(2):
        for c in range(N):
            num_edge = num_edges[r][c]
            if num_edge != e or visited[r][c]:
                continue
            for nr, nc in neighs[r][c]:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    visited[r][c] = 1
                    twos += 1
                    break
    return


funcs = (lambda x: (x[0], (x[1]-1+N) % N),
         lambda x: (x[0] ^ 1, x[1]),
         lambda x: (x[0], (x[1]+1+N) % N))
# 일단 완전 탐색으로 풀어보기.
T = int(input())
for t in range(T):
    N, W = map(int, input().split())
    defence_center = [list(map(int, input().split())) for _ in range(2)]
    neighs = [[None] * N for _ in range(2)]
    num_edges = [[0] * N for _ in range(2)]
    for r in range(2):
        for c in range(N):
            neighs[r][c] = get_neigh(r, c)
            num_edges[r][c] = len(neighs[r][c])
    visited = [[0] * N for _ in range(2)]
    twos, ones = 0, 0
    for i in range(1, 4):
        get_matching(i)
    ones = 2*N - twos * 2
    print(twos+ones)
