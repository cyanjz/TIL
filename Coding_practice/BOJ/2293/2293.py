def solve():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins = list(set(coins))
    DP = [0] * k
    for coin in coins:
        DP[coin] = 1
    for i in range(k):
        for coin in coins:
            if coin <= i:
                DP[i] += DP[i-coin]
    return DP[-1]

def input():
    return f.readline().rstrip('\n')

if __name__ == '__main__':
    f = open(r'test.txt', 'r')
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins = list(set(coins))
    DP = dict()
    solve()
    f.close()