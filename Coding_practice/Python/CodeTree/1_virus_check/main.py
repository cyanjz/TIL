def solve():
    n = int(input())  # number of restaurants
    num_customers = list(map(int, input().split()))
    chief, member = map(int, input().split())
    cnt = 0
    for num_customer in num_customers:
        num_customer -= chief
        if num_customer > 0:
            q, r = divmod(num_customer, member)
            if r:
                cnt += 1
            cnt += q
        cnt += 1
    return cnt

print(solve())
