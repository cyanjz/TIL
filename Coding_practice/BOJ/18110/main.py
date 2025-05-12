# 쓰레기 문제
# 파이썬은 정수부가 짝수일 때와 홀수 일때 반올림 기준이 다름.
import sys
input = sys.stdin.readline


def round(num, d):
    q, r = divmod(num, d)
    if 2*r >= d:
        return q + 1
    else:
        return q


def solve():
    n = int(input())
    if n == 0:
        return 0
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    cut_off = round(len(arr)*15, 100)
    arr = arr[cut_off:len(arr)-cut_off]
    ans = round(sum(arr), len(arr))
    return ans


print(solve())
