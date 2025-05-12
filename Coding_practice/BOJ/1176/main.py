# 간단한 backtracking 문제
import sys
sys.stdin = open('input.txt', 'r')


# depth : 현재 보고 있는 위치
# visited : 현재 포함 여부
# prev : 바로 이전의 학생.
# end condition
# 1. depth = N
# 2. abs(prev - students[cursor]) <= K
# 3. ...
def solve(depth, visited, prev):
    global ans
    if depth == N:
       ans += 1 
       return
    else:
        for i in range(N):
            if not visited[i] and (depth == 0 or abs(prev-students[i]) > K):
                visited[i] = 1
                solve(depth+1, visited, students[i])
                visited[i] = 0
        return


N, K = map(int, input().split())
students = [int(input()) for _ in range(N)]
visited = [0] * N
ans = 0
solve(0, visited, -1)
print(ans)