def dist1(w1, w2):                          # cur, next
    w1r, w1c = wl1[w1]
    w2r, w2c = wl1[w2]
    return abs(w1r-w2r) + abs(w1c-w2c)


def dist2(w1, w2):
    w1r, w1c = wl2[w1]
    w2r, w2c = wl2[w2]
    return abs(w1r-w2r) + abs(w1c-w2c)


def solve():
    # DP[i][j] -> 1번 경찰차가 마지막으로 i+1번 사건, 2번 경찰차가 마지막으로 j+1 번 사건
    # 이때 마지막 사건을 해결하기 까지 남은 이동거리.
    # row -> 1번, col -> 2번
    # DP[W-1][W-1] = 0
    # DP[W-1][:], DP[:][W-1] 또한 0

    # m, n을 업데이트 할 때 next = max(m, n) + 1
    # dp[m][n] = min(dp[next][n]+dist1, dp[m][next]+dist2)
    # dist1 = dist(m, next)
    # DP initialize
    dp = [[0] * (W+1) for _ in range(W+1)]
    trace = [[0] * (W+1) for _ in range(W+1)]
    for i in range(W):
        dp[W][i] = 0
        dp[i][W] = 0

    # DP update
    for i in range(W-1, -1, -1):             # W-2
        for j in range(i+1):
            n = max(i, j) + 1
            dp[i][j] = min(dp[n][j] + dist1(i, n), dp[i][n] + dist2(j, n))
            dp[j][i] = min(dp[n][j] + dist1(j, n), dp[j][n] + dist2(i, n))
        print('#' * N)
        for row in dp:
            print(*row)

    for row in dp:
        print(*row)
    return


N = int(input())
W = int(input())
wl1 = [list(map(int, input().split())) for _ in range(W)]
wl2 = wl1[:]
wl1 = [[1, 1]] + wl1
wl2 = [[N, N]] + wl2
solve()
