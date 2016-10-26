from functools import reduce


def normalize(name):
        return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
r = list(map(normalize, L1))
print(r)
L2 = ['adam', 'LISA', 'barT']
L2.pop(1)
print(L2)


def prod(L):
        return reduce(lambda x, y: x * y, L)


r = prod([3, 5, 9])
print(r)
