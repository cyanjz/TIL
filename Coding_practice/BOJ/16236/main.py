def bfs(shark_size, r, c):
    '''
    :param shark_size:
    상어의 크기
    :param r:
    상어의 현재 위치 (bfs 초기 위치)
    :param c:
    상어의 현재 위치 (bfs 초기 위치)
    :return:
    result - 물고기를 먹은 위치. 먹을 물고기를 못 찾으면 None
    min_d - bfs에서 탐색의 깊이.
    '''
    # 1. bfs에 필요한 변수 선언
    front = -1
    rear = 0
    q = [0] * (N*N)
    q[0] = (r, c)
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1               # visited는 토마토/물 놀이 문제에서 처럼 bfs의 깊이를 구하기 위해 사용됩니다.
    min_c = N
    min_r = N
    min_d = N*N
    found = False   # 먹을 물고기를 찾았으면 bfs 종료해야 하니까, found 변수를 업데이트해줘서 enqueue를 막기.
    result = None
    # 2. 자 이제 bfs를 돌려봅시다.
    # 일반적인 bfs 구조를 따라가되, 인접한 칸들을 enqueue하는 과정에서 문제의 조건을 녹여냅시다!
    while front != rear:
        front += 1          # dequeue
        cr, cc = q[front]   # dequeue
        for dr, dc in ds:   # 인접한 칸들을 보기
            nr, nc = cr + dr, cc + dc
            # 3. 중요한 부분. 문제의 조건을 어떻게 녹여낼지 여기서 꼼꼼하게 작성해야 합니다.
            # 고려해야 할점 - notion의 코멘트 참조
            # 0) 일반적인 bfs의 조건
            # 1) 상어보다 작은 물고기를 찾은 경우
            # 2) 상어와 같은 크기의 물고기를 찾은 경우
            # 3) 상어보다 큰 물고기를 찾은 경우
            # 4) 빈칸을 찾은 경우
            if 0 <= nr < N and 0 <= nc < N:     # 0) bfs 조건
                if not visited[nr][nc]:         # 0) bfs 조건
                    if arr[nr][nc] != 0 and shark_size > arr[nr][nc]:       # 1) 먹을 물고기를 찾음
                        if nr < min_r and visited[cr][cc] + 1 <= min_d:
                            found = True
                            result = (nr, nc)
                            min_d = visited[cr][cc] + 1
                            min_r = nr
                            min_c = nc
                        elif nr == min_r and nc < min_c and visited[cr][cc] + 1 <= min_d:
                            found = True
                            result = (nr, nc)
                            min_d = visited[cr][cc] + 1
                            min_r = nr
                            min_c = nc
                    elif arr[nr][nc] == shark_size or arr[nr][nc] == 0:      # 2) and 4) 탐색 가능한 경우
                        if not found:
                            rear += 1
                            q[rear] = (nr, nc)
                            visited[nr][nc] = visited[cr][cc] + 1
                    else:                                                    # 3) 더 큰 물고기
                        pass
    return result, min_d-1


# main 함수.
# fish가 남아있는 동안 bfs를 반복해서 돌립니다.
# 여기서도 문제의 조건에 유의합시다.
def solve(shark_size, shark_r, shark_c):
    global number_of_fish, number_of_eats
    ans = 0
    while number_of_fish:
        next_coords, dist = bfs(shark_size, shark_r, shark_c)
        if next_coords is None:
            return ans
        else:
            shark_r, shark_c = next_coords
            arr[shark_r][shark_c] = 0
            number_of_fish -= 1
            number_of_eats += 1
            ans += dist
            if number_of_eats == shark_size:
                number_of_eats = 0
                shark_size += 1
    return ans


ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
number_of_fish = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            shark_r, shark_c = r, c
            arr[r][c] = 0
        elif arr[r][c] != 0:
            number_of_fish += 1
shark_size = 2
number_of_eats = 0

print(solve(shark_size, shark_r, shark_c))
