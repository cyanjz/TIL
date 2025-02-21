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
            # compare row/col moves
            row_move1 = dp[n][j] + dist1(i, n)      # 1번 자동차가 움직임
            col_move1 = dp[i][n] + dist2(j, n)      # 2번 자동차가 움직임
            row_move2 = dp[n][i] + dist1(j, n)      # 1번 자동차가 움직임
            col_move2 = dp[j][n] + dist2(i, n)      # 2번 자동차가 움직임
            if row_move1 > col_move1:
                trace[i][j] = 2
                dp[i][j] = col_move1
            else:
                trace[i][j] = 1
                dp[i][j] = row_move1

            if row_move2 > col_move2:
                trace[j][i] = 2
                dp[j][i] = col_move2
            else:
                trace[j][i] = 1
                dp[j][i] = row_move2
        # print('#' * N)
        # for row in dp:
        #     print(*row)
        # print('@' * N)
        # for row in trace:
        #     print(*row)
    # for row in dp:
    #     print(*row)
    # print ans
    print(dp[0][0])
    r = c = 0
    for i in range(W):
        print(trace[r][c])
        if trace[r][c] == 2:
            c = max(r, c) + 1
        else:
            r = max(r, c) + 1
    return


N = int(input())
W = int(input())
wl1 = [list(map(int, input().split())) for _ in range(W)]
wl2 = wl1[:]
wl1 = [[1, 1]] + wl1
wl2 = [[N, N]] + wl2
solve()
