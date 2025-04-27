from copy import deepcopy


def dprint(st):
    if DEBUG:
        print(st)
    else:
        pass


DEBUG = True


def solve():
    # dp는... 이전, 이이전, 남은 갯수
    # dp[x][y][z][prev][pprev]
    # dimension : cnt1, cnt2, cnt3, n, n
    dp = [[0] * n for _ in range(n)]
    for count in counts:
        dp = [deepcopy(dp) for _ in range(count)]
    temp = dp

    dprint(*counts)
    dprint('####')
    for i in range(n+1):
        dprint(len(temp))
        temp = temp[0]
    dprint(len(temp))

    # x, y, z -> hmmmmm
    return


n = int(input())
counts = [int(input()) for _ in range(n)]

print(solve())
