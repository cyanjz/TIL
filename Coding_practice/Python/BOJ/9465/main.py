def solve():
    T = int(input())
    for t in range(T):
        N = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        if N != 1:
            dp = [[0] * 3 for _ in range(2)]
            dp[0][0] = stickers[0][0]
            dp[1][0] = stickers[1][0]
            dp[0][1] = stickers[0][1] + stickers[1][0]
            dp[1][1] = stickers[1][1] + stickers[0][0]
            for c in range(2, N):
                temp = [0, 0]
                for r in range(2):
                    temp[r] = max(dp[r-1][c-1], dp[r-1][c-2]) + stickers[r][c]
            print(max(dp[0][-1], dp[1][-1]))
        else:
            print(max(stickers[0][0], stickers[1][0]))
    return

solve()