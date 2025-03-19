import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')

def solve():
    T = int(input())
    for _ in range(T):
        N, W = map(int, input().split())
        defence = [list(map(int, input().split())) for _ in range(2)]

        # DP 테이블 초기화
        dp = [[0] * 4 for _ in range(N)]

        # 첫 번째 열 초기화
        dp[0][0] = 0  # 아무것도 선택하지 않음
        dp[0][1] = 1 if defence[0][0] + defence[0][-1] <= W else 0  # (0,0)과 (0,N-1) 매칭 가능 여부
        dp[0][2] = 1 if defence[1][0] + defence[1][-1] <= W else 0  # (1,0)과 (1,N-1) 매칭 가능 여부
        dp[0][3] = 1 if defence[0][0] + defence[1][0] <= W else 0  # (0,0)과 (1,0) 매칭 가능 여부

        for i in range(1, N):
            dp[i][0] = max(dp[i-1])  # 아무것도 선택하지 않은 경우
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + (1 if defence[0][i] + defence[0][i-1] <= W else 0)
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + (1 if defence[1][i] + defence[1][i-1] <= W else 0)
            dp[i][3] = dp[i-1][0] + (1 if defence[0][i] + defence[1][i] <= W else 0)

        # 결과 출력
        print(max(dp[N-1]))

solve()
