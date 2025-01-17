def solve():
    while coins:
        coin = coins.pop()
        for i in range(1, k//coin+1):
            DP[coin * i] = min(DP.get(coin*i, k), i)
        for K, V in DP.items():
            DP[K] = min(V, DP.get(K-coin, k) + 1)
    print(DP)
    return

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