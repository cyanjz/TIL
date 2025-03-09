from collections import deque


def get_lis():
    global mountains
    result = deque([0] * N)
    # 높이가 i 인 최장 수열.
    # 근데 이거 업데이트 하는데 소요 좀 많이 되겠는데
    # 왼쪽에 있는 산 중에서 가장 길이가 긴 산을 찾아서 해당 값 + 1 로 업데이트.
    # 너무 높은 산이 나오면 scope가 너무 커진다. 그냥 순회하는게 나을 것 같다.
    # O(N * M)
    # 그럼 안쓰면 쭉 보는걸 계속 해야하는디? -> O(1 + 2 + 3 + 4... N) = O(N**2)
    # max_length = [0] * 1000000
    for i in range(N):
        # largest_increasing : 현재 위치, i 보다 왼쪽에 있으면서 최장 증가인 수열의 길이
        largest_increasing = 0
        for j in range(i):          # i 이전의 index 순회
            if mountains[j] < mountains[i] and largest_increasing < result[j]:      # 작으면서 더 긴 경우
                largest_increasing = result[j]
        result[i] = largest_increasing + 1
    return result


# 100
def big_bang(n, *heights):
    return n, deque(heights)


# 200
# LIS 업데이트
# 왼쪽에 있으면서 새로운 산보다 작으면서 가장 긴 녀석 + 1로 할당.
def add_mountain(h):
    global mountains, LIS, N
    mountains.append(h)
    LIS.append(0)
    largest_increasing = 0
    for i in range(N):
        if mountains[i] < h and largest_increasing < LIS[i]:
            largest_increasing = LIS[i]
    N += 1
    return


# 300
def earthquake():
    global mountains, LIS
    mountains.pop()
    LIS.pop()
    return


# 400
# LIS 찾기.
# LIS 찾아도 문제되는게 케이블카를 타는 경우가 문제임.
# LIS를 찾아서 [3, 2, 1, 0] 이런식이면 3을 선택하는게 맞기는 한데
# 케이블카가 중간에 있으면 어떻게 해야하나. -> 무조건 타야지
# LIS 만드는데에도 시간 소모가 극심하다.
# 그럼... 흠.... 한번 만들고 계속 사용?
# LIS 만들고 업데이트를 계속 하기
# 최장 증가 수열을 가지고 있기는 해야해.
# 근데 업데이트를 어떤식으로 할지가 문제야
# 최장 증가 수열은 어떻게 작업해야 할까
# 배열로 관리 -> 업데이트를 할 때 어떤 최장 증가 수열에 영향을 주는지 생갹해야함.
# 어... 잘 생각해보니까 들어온 원소만 바뀌면 되네요!
# 왼쪽에 있으면서 새로운 산보다 작으면서 가장 긴 녀석 + 1로 할당.
# 그럼 들어온 원소의 LIS
# 2 3 5 (3) -> 1, 2, 3, 2
# 2 3 5 (4) -> 1, 2, 3, 3
# 2 3 5 (6) -> 1, 2, 3, 4
# 들어온 숫자보다 작은 애들을 쪽
# 1. 업데이트 :
    #
# 2.

def climb_simulation(m_index):
    global mountains
    m_index -= 1

    return


func_dict = {100: big_bang, 200: add_mountain, 300: earthquake, 400: climb_simulation}
Q = int(input())
# big bang, initialize mountains
cmd_type, *params = list(map(int, input().split()))
N, mountains = func_dict[cmd_type](*params)
LIS = get_lis()
print(LIS)
# for q in range(Q):
#     cmd_type, *params = list(map(int, input().split()))
#     func_dict[cmd_type](*params)
