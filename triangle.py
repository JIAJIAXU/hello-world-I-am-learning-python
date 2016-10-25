def triangles(n):
    L = [1]
    while True:
        yield L
        L = [1] + [L[x - 1] + L[x] for x in range(1, len(L))] + [1]
        n = n - 1
        if n < 0:
            break
for t in triangles(4):
    print(t)


def t(x):
    N = [1]
    n = 0
    while n <= x:
        print(N)
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(len(N))]
        n = n + 1
t(4)
