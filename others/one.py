list_funcs = [lambda x: x**2, lambda x: x*2]

closure = lambda x: ((lambda y: y**x)(y) for y in [1, 2, 3, 4, 5])

for i in closure(11):
    print(i)


def der(aaa): return aaa + 1
print(der(1))