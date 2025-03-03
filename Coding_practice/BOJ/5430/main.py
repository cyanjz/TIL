def solve():
    cmds = input()
    cmds = ''.join(cmds.split("RR"))
    N = int(input())
    temp = input()[1:-1].split(',')
    if not temp[0]:
        arr = []
    else:
        arr = temp
    pivot = 0
    for cmd in cmds:
        if cmd == 'R':
            pivot = ~pivot
        else:
            if arr:
                arr.pop(pivot)
            else:
                return 'error'
    if pivot:
        arr = arr[::-1]
    arr_string = '[' + ','.join(arr) + ']'
    return arr_string


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print(solve())