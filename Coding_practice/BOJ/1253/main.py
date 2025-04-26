# N ** 3 = 8E9 (불가능)
# 한번의 GOOD 여부 판별을 N만에 찾아야 함.
# 그럼... start, end 놓고 범위를 줄여가기.

def solve():
    cnt = 0
    length = len(numbers)
    for i in range(N):
        # 현재 판별 중인 숫자.
        target = numbers[i]
        s = 0
        e = length - 1
        while s < e:
            cursor = numbers[s] + numbers[e]
            # 1. 같으면 찾은 경우.
            # 이 경우에는 cnt++
            if cursor == target:
                if s == i:
                    s += 1
                elif e == i:
                    e -= 1
                else:
                    cnt += 1
                    break
            # 2. cursor가 target보다 크면 e -= 1
            elif cursor > target:
                e -= 1
            # 3. cursor가 target보다 작으면 s += 1
            elif cursor < target:
                s += 1
    return cnt


N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(solve())
