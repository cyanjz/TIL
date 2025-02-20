def solve1():
    N = int(input())
    arr = list(map(int, input().split()))
    inc = [0] * N
    dec = [0] * N
    for i in range(1, N):
        j = N-1 - i
        # i의 왼쪽에서 arr[i] 보다 작으면서 가장 긴 증가 수열 찾기
        max_len = -1
        for k in range(i-1, -1, -1):
            # arr[i]보다 작으면서 길이가 가장 큰 것을 찾기.
            if arr[k] < arr[i] and inc[k] > max_len:
                max_len = inc[k]
        inc[i] = max_len + 1
        # j의 오른쪽에서 arr[j] 보다 작으면서 가장 긴 감소 수열 찾기
        max_len = -1
        for k in range(j+1, N):
            # arr[j]보다 작으면서 길이가 가장 큰 것을 찾기.
            if arr[k] < arr[j] and dec[k] > max_len:
                max_len = dec[k]
        dec[j] = max_len + 1
    return max([inc[i] + dec[i] for i in range(N)]) + 1


print(solve1())
