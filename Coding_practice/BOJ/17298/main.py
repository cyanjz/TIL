def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    nge = [-1] * N
    top = -1
    stack = [(0, 0)] * N  # idx, num
    for i in range(N):
        num = arr[i]
        while top >= 0 and stack[top][1] < num:
            nge[stack[top][0]] = num
            top -= 1
        top += 1
        stack[top] = (i, num)
    return nge

if __name__ == '__main__':
    print(*solve())