# 알고리즘 설계
# 1. 배열을 양수와 음수부로 나눈다
# 2. 배열의 양수와 음수부에서 최댓값을 계산하고, 큰 쪽을 마지막으로 가기
#   1) 양수/음수 둘 중 하나만 있는 경우에는 해당 방향을 마지막으로 가기.
#   2) 양수/음수 둘다 존재하는 경우에는 둘 중 최대값이 큰 쪽을 마지막으로 가기.
# 그리디 탐색 규칙 탐구
# 1. 기본 규칙
# 특정 방향으로 M개의 책을 가지고 가게되면, 가장 멀리 가야하는 책을 기준으로 M개의 책을 한번에 반환할 수 있기 때문에,
# max_dist * 2만큼의 거리만 있으면 M개의 책을 모두 제자리에 둘 수 있다.
# 예를 들어, [3, 10, 15, 20]이고 M == 3인 경우에는 20, 15, 10 책을 가지고 가면 40의 거리로 3개의 책을 제자리에 둘 수 있다.
# 2. 그리디 규칙
# 특정 방향을 마지막으로 가면, 해당 방향의 가장 큰 M개의 요소는 다시 돌아올 필요가 없기 때문에,
# *2가 아닌 *1한 값을 더해주면 된다.
# 양수부의 거리가 가장 먼 책과 음수부의 거리가 가장 먼 책 둘 중에서 더 멀리 있는 책을 왕복하지 않는게 유리하기 때문에,
# 양수부와 음수부의 max값을 비교하고 더 큰 방향에서 M개를 제외하고 step을 계산한다.
# 3. 예제
# [-39, -37, -29, -28, -6, 2, 11]
# -39, -37을 마지막에 둔다.
# 나머지 [-29, -28, -6, 2, 11]을 최소 거리로 두는 방법은,
# -29, -28을 가지고 가서 제자리에 놓고, -6을 가지고 가서 제자리에 놓고,
# 11, 2를 가지고 가서 제자리에 놓는 것임.
# 따라서, 39 + (29+6+11) * 2 = 131이 정답이다.
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# flag=1인 경우에는 M개의 요소를 제외하고 step을 계산.
# flag=0인 경우에는 바로 step을 계산.
# 여기서 M개의 요소를 제외할 수 없는 경우가 걱정될 수 있는데, 그 경우에는 while의 i >= 0 조건에 바로 걸리기 때문에 문제 없음.
def get_steps(book_dist, flag):
    arr_len = len(book_dist)
    if flag:
        result = max(book_dist)
        i = arr_len - 1 - M
    else:
        result = 0
        i = arr_len - 1
    while i >= 0:
        result += book_dist[i] * 2
        i -= M
    return result


def solve():
    # 0. 기초 변수 할당
    ans = 0
    # 1. 배열을 양수/음수 나누기.
    arr_minus = [-x for x in arr if x < 0]
    arr_plus = [x for x in arr if x > 0]
    arr_minus.sort()
    arr_plus.sort()
    # 2. case 별로 값을 반환
    if not arr_minus:                   # 1) 음수가 없는 경우
        return get_steps(arr_plus, 1)
    elif not arr_plus:                  # 2) 양수가 없는 경우
        return get_steps(arr_minus, 1)
    else:                               # 3) 두 값을 비교해서 큰 쪽을 제외하기.
        minv = max(arr_minus)
        maxv = max(arr_plus)
        if maxv > minv:
            return get_steps(arr_plus, 1) + get_steps(arr_minus, 0)
        elif minv > maxv:
            return get_steps(arr_plus, 0) + get_steps(arr_minus, 1)


N, M = map(int, input().split())
arr = list(map(int, input().split()))

front = -1
rear = N-1
print(solve())
