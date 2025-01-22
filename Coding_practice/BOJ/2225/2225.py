if __name__ == "__main__" :
    N, K = map(int, input().split())
    dp = [0] * K
    dp[0] = 1
    temp = dp
    for i in range(1, N):
        temp = [1] + dp[:-1]
        dp = list(map(lambda x, y : x + y, temp, dp))
    number_of_combinations = K
    ans = number_of_combinations * temp[0]
    for i in range(1, K):
        number_of_combinations *= (K-i)
        number_of_combinations //= (1+i)
        ans += (number_of_combinations * temp[i])
    print(ans%1000000000)