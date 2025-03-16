# 1. 필요한 자료구조
# 1) tree : segment tree. 각 height 별로 lis값을 가지고 있는 arr에 대한 seg tree
# 2) ans : 특정 index의 lis를 저장하고 있는 배열. stack.
# 3) mountains : 특정 index의 산의 높이를 저장하고 있는 배열. stack

# 2. 알고리즘
# 1) add_mountain
#   1> mountains에 새로운 산을 업데이트
#   2> tree의 height값을 갱신
#   3> ans에 새로 들어온 index의 lis 값 갱신하기.
#       1] height가 더 큰 쪽이 들거아함. 왜냐하면 산의 높이가 높은 쪽이 답이니까.
# 2) earth_quake
#   1> mountains pop 수행
#   2> ans pop 수행
#   3> ans의 마지막 요소 -> (height, lis - 1) 해당 index의 이전 lis를 기반으로 tree를 업데이트 해줘야함.
#       1] ans에 저장될 값들은, 해당 height가 추가되기 이전의 lis 값을 저장.
import sys
sys.stdout = open('edge.txt', 'w')

QMAX = 500000

print(QMAX)
print(100, end=' ')
for i in range(QMAX):
    print(1000000, end=' ')
print()
for i in range(QMAX-2):
    print(200, 1000000)
print(400, 2)
