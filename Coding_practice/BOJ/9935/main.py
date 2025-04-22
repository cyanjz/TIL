line = input()
bomb = input()

stack = [0] * len(line)
top = -1
N = len(bomb)
pivot = N - 1
for c in line:
    # push
    top += 1
    stack[top] = c
    # check
    for i in range(N):
        if stack[top-i] != bomb[N-1-i]:
            break
    else:
        # pop N elements
        top -= N
if top == -1:
    print('FRULA')
else:
    print("".join(stack[:top+1]))