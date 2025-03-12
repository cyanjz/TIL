# 알고리즘 구상.
# 1. bf는 불가능.
# start와 end를 다 순회해보기.
# 2^100000 -> 가능한 모든 부분 집합에 대한 가능성 탐색.
# 2. 정렬하기
# 정렬하면 처음부터 보면서 겹치는 부분을 추적하기.
#   1) start로 정렬한 배열과 end로 정렬한 배열?
#       두 개의 배열을 관리하면, 두 배열간의 관계를 추적하기 어렵다.
#   2) start로 정렬한 배열
#       여기서 start는 해당 사람의 출발지와 도착지 중에서 작은 값으로 맞춰준다.
# 기차가 특정 범위의 사람들을 포함하면, 무조건 범위내의 특정 사람의 시작점에서 출발해도 무관하다.
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def solve():
    ans = 0
    for i in range(N):
        # 가능한 case 순회하면서 정답 찾아나가기.
        cnt = 0                     # 현재 위치를 포함할 때 포용 가능한 사람의 수
        j = i                       # 탐색을 위한 index
        s, e = people[i]            # 현재 참조하는 사람의 정보
        s_upper_bound = s + D       # s에서 시작하니 끝점의 upper bound는 s+D.
        while j < N:
            s, e = people[j]
            # 현재 주어진 끝점이 e의 upper bound보다 큰 경우
            if s > s_upper_bound:
                break
            if e <= s_upper_bound:
                cnt += 1
            j += 1
        ans = max(ans, cnt)
        if ans == N:
            return ans
    return ans


# 1. 입력 받고 정렬하기.
N = int(input())
people = [sorted(list(map(int, input().split()))) for _ in range(N)]
people.sort(key=lambda x : x[0])
D = int(input())
# 2. solve 호출.
print(solve())
