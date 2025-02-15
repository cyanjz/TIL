from collections import deque
import sys

input = sys.stdin.read
def solve():
    data = input().split("\n")
    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N, K = map(int, data[index].split())
        index += 1
        build_times = list(map(int, data[index].split()))
        index += 1

        # 그래프 초기화
        in_degree = [0] * N
        build_path = [[] for _ in range(N)]
        for _ in range(K):
            r, c = map(lambda x: int(x)-1, data[index].split())
            index += 1
            build_path[r].append(c)
            in_degree[c] += 1  # 진입 차수 증가

        W = int(data[index]) - 1  # 목표 건물
        index += 1

        # 위상 정렬 (BFS)
        dp = [0] * N
        queue = deque()

        # 진입 차수가 0인 건물부터 시작
        for i in range(N):
            if in_degree[i] == 0:
                queue.append(i)
                dp[i] = build_times[i]  # 최초 건설 시간

        while queue:
            sp = queue.popleft()
            for nb in build_path[sp]:
                dp[nb] = max(dp[nb], dp[sp] + build_times[nb])  # 최적의 시간 계산
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    queue.append(nb)

        results.append(str(dp[W]))

    print("\n".join(results))

solve()