def solve():
    return


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        cores = []
        d_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(N):
            for c in range(N):
                if arr[r][c]:
                    cores.append((r, c))

        print(f'#{t+1} {solve()}')
