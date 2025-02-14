from collections import deque
import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# solve1 -> BFS 사용하여 모든 경우의 수 판별하기.
def solve1():
    N, K = map(int, input().split())
    # 빌드 타임 읽어오기.
    build_times = list(map(int, input().split()))
    
    # build path dictionary와 시작지점 만들기
    build_path = {k: [] for k in range(N)}  # key : 선행 조건. value : 지을 수 있는 건물 목록.
    pre_requests = [0] * N  # idx : 건물. elem : 필요한 선행 요건 수.
    for _ in range(K):
        r, c = map(lambda x : int(x)-1, input().split())  # 선행 요건, 건물.
        build_path[r].append(c)
        pre_requests[c] += 1
    # 목표 건물 읽어오고 dp 초기화.
    W = int(input()) - 1  # 목표 건물 idx.
    dp = [0] * N  # 짓기 시작하기 위한 최소 시간.
    dump = deque([i for i in range(N) if not pre_requests[i]])

    # DP update.
    while dump:
        sp = dump.popleft()
        for nb in build_path[sp]:  # nb : next buildings, sp : cursor
            # nb의 선행 조건을 모두 확인 했다면 dump에 추가하기.
            dp[nb] = max(dp[nb], dp[sp] + build_times[sp])
            pre_requests[nb] -= 1
            if not pre_requests[nb]:
                dump.append(nb)
    return dp[W] + build_times[W]


T = int(input())
for t in range(T):
    print(solve1())
