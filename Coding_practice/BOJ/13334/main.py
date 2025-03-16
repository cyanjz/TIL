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
import heapq
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


# 시간 복잡도 : 10,000,000,000 = 100억. (불가능)
# 그럼 어떻게 최적화를 할 수 있을까?
# end 순으로 정렬된 배열을 봐야하나?
# -> start와 end가 모두 범위에 포함되어야 하므로로, end 순으로 본다고 해도 어렵다.
# 마지막으로 포함할 수 없었던 사람을 포함할 수 있으면 탐색할 가치가 있고, 아니면 SKIP.
# 끝점 정렬이 필요한 건 확실해 보이는데, 이걸 어떻게 시작점 얼렬과 이어줄 것인가?
# 끝점 정렬을 기준으로 탐색을 수행하기. -> 시작점이 초과할 수 있다.

# heap 사용
# 시간 복잡도 : O(nlogn)
# 아이디어 : end를 기준으로 정렬된 집과 사무실 배열에서 s, e를 읽어오면서
# s를 min heap에 enqueue.
# enqueue 수행 이후에는 시작 지점이 e-D보다 큰 값만 남겨야 하므로
# e-D가 heap의 root보다 큰 동안 계속해서 dequeue
# dequeue가 끝나면 heap의 크기를 바탕으로 정답 업데이트.
def solve():
    heap = []
    ans = 0
    lower_bound = -100000000
    for s, e in people:
        heapq.heappush(heap, s)
        lower_bound = e - D
        while len(heap) != 0 and e-D > heap[0]:
            heapq.heappop(heap)
        ans = max(len(heap), ans)
    return ans


# 1. 입력 받고 정렬하기.
# 끝점 기준으로 정렬하고, 끝점이 같으면 시작점 기준으로 정렬
N = int(input())
people = [sorted(list(map(int, input().split()))) for _ in range(N)]
people.sort(key=lambda x: (x[1], x[0]))
D = int(input())
# 2. solve 호출.
print(solve())
