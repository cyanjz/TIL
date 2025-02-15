def eval_equation(eq):
    ans = eq[0]
    pivot = 1
    print(ans)
    while pivot+2 <= len(eq):
        ans = eval(f'{ans}{eq[pivot:pivot+2]}')
        print(ans)
        pivot += 2
    return ans

print(eval_equation('3+8*7-9*2'))