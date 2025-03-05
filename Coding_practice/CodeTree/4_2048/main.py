# class Stack:
#     def __init__(self, size):
#         self.top = -1
#         self.stack = [0] * size
        
#     def push(self, e):
#         self.top += 1
#         self.stack[self.top] = e
        
#     def pop(self):
#         result = self.stack[self.top]
#         self.top -= 1
#         return result
    
#     def peek(self):
#         return self.stack[self.top]


def tilt_left(temp):
    for r in range(N):
        non_zeros = [num for num in temp[r] if num != 0]
        new_row = [0] * N
        top = -1
        # 숫자가 하나밖에 없는 경우.
        if len(non_zeros) == 1:
            new_row[0] = non_zeros[0]
        # 숫자가 하나 이상 있는 경우
        else:
            
    return 


def dfs(depth):
    global arr
    if depth == 5:
        cur_score = max([max(row) for row in arr])
        ans = max(ans, cur_score)
        return
    else:
        for row in arr:
            pass


N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# dfs()
# print(ans)


arr = [[4, 2, 0, 8], [4, 2, 2, 4], [0, 8, 8, 2], [4, 2, 2, 2]]
tilt_left(arr)
for row in arr:
    print(*row)