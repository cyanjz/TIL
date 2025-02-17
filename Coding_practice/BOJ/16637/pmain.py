def get_comb(arr, temp, start = 0):
    global combinations
    if start >= len(arr)-1:
        combinations.append(temp)
        return 
    else:
        combinations.append(temp[:])
        for i in range(start, len(arr)-1):
            temp.append(arr[i])
            get_comb(arr, temp[:], i+2)
            temp = temp[:-1]
    return combinations


def get_equation(comb, eq):
    eq_list = [c for c in eq]
    if not comb:
        return eq_list
    try:
        temp = [eval(''.join(eq[idx:idx+3])) for idx in comb]
    except:
        breakpoint()
    for i in range(len(comb)-1, -1, -1):
        idx = comb[i]
        for _ in range(2):
            eq_list.pop(idx)
        eq_list[idx] = temp[i]
    return eq_list


def eval_equation(eq):
    pivot = 1
    ans = int(eq[0])
    while pivot < len(eq):
        try:
            ans = eval(f'{ans}{eq[pivot]}{eq[pivot+1]}')
        except:
            print(ans)
        pivot += 2
    return ans


def solve():
    N = int(input())
    eq = input()
    if N == 1:
        print(eq[0])
        return
    idicies = [i for i in range(0, N, 2)]
    combs = get_comb(idicies, [])
    max_value = -2e31
    for comb in combs:
        eq_list = get_equation(comb, eq)
        cur_value = eval_equation(eq_list)
        if cur_value > max_value:
            max_value = cur_value
    print(max_value)
    return


if __name__ == '__main__':
    combinations = []
    solve()
