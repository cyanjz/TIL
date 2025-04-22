<<<<<<< HEAD
def max_area(arr, N):
    max_s = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                s = 0
                for ni in range(i, N):
                    if arr[ni][j] == 0:
                        break
                    for nj in range(j, N):
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                            s += 1
                        else:
                            break
                if max_s < s:
                    max_s = s
    return max_s

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {max_area(square, N)}")
=======
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    population = list(map(int,input().split()))

    town = [i for i in range(N)]
    min_diff = sum(population)

    # 마을의 부분집합을 만든다.
    subsets = []
    for num in range(1<<N-1): # num 은 2의 N 승까지의 이진수
        subsets.append([])
        for i in range(N):  # i 마을은 포함 될 것인가?
            if num & (1 << i):  # num 의 i번째 숫자가 0인지 1인지 체크 - 1이면 포함된다
                subsets[num].append(i)

    for subset in subsets:  # 모든 부분집합에 대해 체크

        complement = [i for i in range(N) if i not in subset]   # 여집합 생성

        # 해당 부분집합이 유효한 지역구인지 판별한다.
        ## 어떻게 할 것인가? 예를 들어서 마을이 1,2,3
        ## 1에서 출발 - 가능한 모든 마을을 탐색 / 이때 마을 중에 있어야만 이동
        subset_mod = subset[:]
        for town_1 in subset:
            for town_2 in range(N):
                if arr[town_1][town_2]==1:  # 두 마을이 연결되어 있다면,
                    if town_2 in subset_mod:
                        subset_mod.remove(town_2)       ## 이동한 마을은 삭제
        ## 전부 돌았을때 영집합이 되었는지 / 혹은 부분집합의 원소가 하나여도 가능하다
        if not subset_mod or len(subset)==1:

            # 그럼 여집합에 대해서도 체크한다
            complement_mod = complement[:]
            for town_1 in complement:
                for town_2 in range(N):
                    if arr[town_1][town_2] == 1:  # 두 마을이 연결되어 있다면,
                        if town_2 in complement_mod:
                            complement_mod.remove(town_2)  ## 이동한 마을은 삭제
            if not complement_mod or len(complement)==1:

                # 유권자 차이 계산
                subset_sum, complement_sum = 0,0
                for s in subset:
                    subset_sum += population[s]
                for c in complement:
                    complement_sum += population[c]
                diff = abs(subset_sum-complement_sum)

                if min_diff > diff:
                    if diff == 5:
                        print(subset)
                    min_diff = diff

    print(f'#{tc} {min_diff}')

>>>>>>> efa015853d09c5f8694479c64a6e7e2d7e2c32f8
