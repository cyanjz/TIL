# 1. 가능한 모든 조합들을 고려해보고... 조합들을 통해 값을 찾기.
# - 조합의 수가 너무 많아서 불가능할 것 같음.
# 2. 그럼...
# - weights가 정렬되어 있으니까
# - weights의 w에 대해서 하나씩 올려보기?
# - 

def solve():
    for w in weights:

    return


N = int(input())
weights = list(map(int, input().split()))
weights.sort()
