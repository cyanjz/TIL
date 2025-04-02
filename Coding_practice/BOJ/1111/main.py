def solve():
    if N == 1:
        return 'A'
    arr = list(map(int, input().split()))
    if N == 2:
        if arr[0] == arr[1]:
            return arr[0]
        else:
            return 'A'
    if N >= 3:
        if arr[0] == arr[1]:
            a, r = 0, 0
        else:
            a, r = divmod((arr[1]-arr[2]), (arr[0]-arr[1]))
        if r:
            return 'B'
        else:
            b = arr[1] - arr[0] * a
            for i in range(N-1):
                if arr[i] * a + b != arr[i+1]:
                    return 'B'
            return arr[N-1] * a + b


N = int(input())
print(solve())
