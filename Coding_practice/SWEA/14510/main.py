# import sys
# sys.stdin = open('Sample_input.txt', 'r')
# sys.stdout = open('o.txt', 'w')
def get_date(a, b):
    if a > b:
        return 2 * a - 1
    else:
        return 2 * b


T = int(input())
for t in range(T):
    N = int(input())
    trees = list(map(int, input().split()))
    max_height = max(trees)
    ans = [0, 0]
    for tree in trees:
        diff = (max_height - tree)
        q, r = divmod(diff, 2)
        ans[0] += r
        ans[1] += q
    while ans[1]:
        diff = ans[1] - ans[0]
        if diff <= 1:
            break
        else:
            ans[1] -= 1
            ans[0] += 2
    print(f'#{t+1} {get_date(ans[0], ans[1])}')
