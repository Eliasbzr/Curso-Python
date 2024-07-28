# Yield From

def gen1():
    yield 1
    yield 2
    yield 3

def gen2 ():
    yield from gen1()
    yield 4
    yield 5


g = gen2()
for n in g:
    print(n)

# Serve para executar os yiels em ordem, posso referenciar um yiel chamando outro
# é possivel dar continuidade em num yield no outro
