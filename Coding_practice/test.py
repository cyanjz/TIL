def max_area(arr, N):
    max_s = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                s = 0
                for ni in range(i, N):
                    if arr[ni][j] == 0:
                        break
                    for nj in range(j, N):
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                            s += 1
                        else:
                            break
                if max_s < s:
                    max_s = s
    return max_s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {max_area(square, N)}")
