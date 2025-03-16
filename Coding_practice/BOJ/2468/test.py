def a():
    v = [0] * 10
    b(v)
    print(v)


def b(v):
    v[0] = 100


a()
