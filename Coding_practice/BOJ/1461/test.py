import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(*sorted(arr))
