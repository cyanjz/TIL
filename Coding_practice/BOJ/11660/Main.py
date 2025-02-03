N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

def solve():
    sum_matrix = [[0] * (N+1)] + [[0] + [table[r][0]] + [0]*(N-1) for r in range(N)]
    for r in range(1, N+1):
        for c in range(1, N+1):
            sum_matrix[r][c] = sum_matrix[r][c-1] + table[r-1][c-1]
    for c in range(1, N+1):
        for r in range(1, N+1):
            sum_matrix[r][c] = sum_matrix[r-1][c] + sum_matrix[r][c]
    for _ in range(M):
        r1, c1, r2, c2 = map(int, input().split())
        print(sum_matrix[r2][c2]-sum_matrix[r2][c1-1]-sum_matrix[r1-1][c2]+sum_matrix[r1-1][c1-1])
    

if __name__ == '__main__':
    solve()