def bf():
    return

N, K = map(int, input().split())
words = [input() for _ in range(N)]
bits = 1 << 26
ans = 0
for c in ['a', 'n', 'c', 't', 'i']:
    bits |= 1 << ord(c)-ord('a')
bf()
