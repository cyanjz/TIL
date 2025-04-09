import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('o.txt', 'w')


def argmax(death):
    max_g = -float('inf')
    max_idx = -1
    for i in range(N):
        if (1 << i) & death:
            continue
        if max_g < guilty[i]:
            max_g = guilty[i]
            max_idx = i
    return max_idx


# 종료 조건
# 1. 은진이 사망
# 2. 모든 사람을 죽임
# 인자
# 1. depth
# 2. death : 죽은 사람.
# 3. num_people : 짝수 홀수에 따라서 로직 다르게 작성.
def solve(death, num_people, nights):
    global ans
    g = guilty
    # 종료 조건 0 최댓값 찾음
    if ans == max_night:
        return
    # 종료 조건 1 은진 사망
    if death & (1 << jin):
        ans = max(ans, nights)
        return
    # 종료 조건 2 모든 사람이 죽음
    if num_people == 1:
        ans = max(ans, nights)
        return
    # 재귀 호출
    # odd, day
    if num_people % 2:
        max_idx = argmax(death)
        solve(death + (1<<max_idx), num_people - 1, nights)
    # even, night
    else:
        for i in range(N):
            if (1 << i) & death or i == jin:
                continue
            for j in range(N):
                guilty[j] += arr[i][j]
            solve(death + (1<<i), num_people - 1, nights+1)
            for j in range(N):
                guilty[j] -= arr[i][j]


N = int(input())
guilty = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
jin = int(input())
ans = 0
max_night = N//2
solve(1 << N, N, 0)
print(ans)
