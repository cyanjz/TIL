<<<<<<< HEAD
T = int(input())    # bus_route
for br in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))
    bus_stop = [0]*(N+1)    # 버스 정류장 배열
    for c in charge_stop:
        bus_stop[c] = 1     # 충전기 인덱스 1 할당

    i = 0 # 현재 위치 초기화
    min_charge = 0  # 최소 충전 횟수
    while i+K < N: # 종점 도달 전까지 반복
        for j in range(i+K, i, -1):     # 도달 가능 범위에서 역순 탐색
            if bus_stop[j] == 1:    # 도달 가능 범위에 충전소o
                i = j
                min_charge += 1
                break
            else:   # 도달 가능 범위 충전소x
                min_charge = 0
                break

    print(f"#{br} {min_charge}")
=======
import sys


sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

print(sys.stdin.readline().rstrip())
print(sys.stdin.readline())
print(sys.stdin.readline())
>>>>>>> bccdbf41e9f9d6013b024f2c9ede23af862bb6fe
