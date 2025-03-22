import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def check(r1, c1, r2, c2):
    return arr[r1][c1] + arr[r2][c2] <= W


def solution():
    a, b, d, e = 0, 0, 0, 0
    c = N-1
    # 0, 0 and 0, N-1 연결
    if arr[0][0] + arr[0][N-1] <= W:
        dp = [[0] * N for _ in range(4)]
        dp[1][0] = 1
        dp = solve(dp)
        dp[0][c] = max(dp[r][c-1] for r in range(4))
        dp[2][c] = max(dp[0][c-1], dp[1][c-1]) + 1 if check(1, c-1, 1, c) else 0
        dp[3][c] = dp[0][c] + 1 if check(0, c, 1, c) else 0
        a = max(dp[r][c] for r in range(4))
    # 1, 0 and 1, N-1 연결
    if arr[1][0] + arr[1][N-1] <= W:
        dp = [[0] * N for _ in range(4)]
        dp[2][0] = 1
        dp = solve(dp)
        dp[0][c] = max(dp[r][c-1] for r in range(4))
        dp[1][c] = max(dp[0][c-1], dp[2][c-1]) + 1 if check(0, c-1, 0, c) else 0
        dp[3][c] = dp[0][c] + 1 if check(0, c, 1, c) else 0
        b = max(dp[r][c] for r in range(4))
    # 0, 0 and 1, 0 연결
    if arr[0][0] + arr[1][0] <= W:
        dp = [[0] * N for _ in range(4)]
        dp[3][0] = 1
        dp = solve(dp)
        dp[0][c] = max(dp[r][c-1] for r in range(4))
        dp[1][c] = max(dp[0][c-1], dp[2][c-1]) + 1 if check(0, c-1, 0, c) else 0
        dp[2][c] = max(dp[0][c-1], dp[1][c-1]) + 1 if check(1, c-1, 1, c) else 0
        dp[3][c] = dp[0][c] + 1 if check(0, c, 1, c) else 0
        d = max(dp[r][c] for r in range(4))
    # 연결을 하나도 안하는 경우
    dp = [[0] * N for _ in range(4)]
    dp = solve(dp)
    dp[0][c] = max(dp[r][c - 1] for r in range(4))
    dp[1][c] = max(dp[0][c - 1], dp[2][c - 1]) + 1 if check(0, c - 1, 0, c) else 0
    dp[2][c] = max(dp[0][c - 1], dp[1][c - 1]) + 1 if check(1, c - 1, 1, c) else 0
    dp[3][c] = dp[0][c] + 1 if check(0, c, 1, c) else 0
    e = max(dp[r][c] for r in range(4))
    return max(a, b, d, e)


def solve(dp):
    # 1. dp[0][c] : c열은 매칭 없음.
    #   - 모두 가능하니까, dp[:][c-1]의 최댓값 사용.
    # 2. dp[1][c] : 위쪽 행만 사용. dp[0][c-1]과 dp[0][c]의 매칭.
    #   - dp[2][c-1]과 dp[0][c-1]의 최댓값 사용.
    # 3. dp[2][c] : 아래쪽 행만 사용. dp[1][c-1]과 dp[1][c]의 매칭.
    #   - dp[1][c-1]과 dp[0][c-1]의 최댓값 사용.
    # 4. dp[3][c] : 세로 매칭. dp[0][c]와 dp[1][c]의 매칭.
    #   - dp[3][c-1] 과 dp[0][c-1]의 최댓값 사용.
    # dp 에는 최대 쌍의 갯수를 저장. 즉, c 번째 열까지 봤을 때 가능한 경우의 수에 따라 최댓값을 기록.
    for c in range(1, N-1):
        dp[0][c] = max(dp[r][c-1] for r in range(4))
        dp[1][c] = max(dp[0][c-1], dp[2][c-1]) + 1 if check(0, c-1, 0, c) else 0
        dp[2][c] = max(dp[0][c-1], dp[1][c-1]) + 1 if check(1, c-1, 1, c) else 0
        dp[3][c] = dp[0][c] + 1 if check(0, c, 1, c) else 0
    return dp


T = int(input())
for t in range(T):
    N, W = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2)]
    twos = solution()
    print(2 * N - twos)
