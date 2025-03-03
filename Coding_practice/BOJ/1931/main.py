import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
# start, end
schedules = [list(map(int, input().split())) for _ in range(N)]
schedules.sort(key=lambda x : (x[1], x[0]))
end_time = 0
ans = 0
for s, e in schedules:
    # start time이 현재의 끝나는 시간보다 뒤인 경우
    if s >= end_time:
        end_time = e
        ans += 1
print(ans)
