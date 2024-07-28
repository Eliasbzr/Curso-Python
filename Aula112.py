# Filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},]

# list comprehenshion
# novos_produtos = [
#     p for p in produtos
#     if p['preco'] >10
# ]

novos_produtos = filter(
    lambda p: p['preco'] >25, #aqui é o filtro
    produtos #aqui é onde sera filtrado
)
# tbm posso usar o filter baseado em uma funcao
def filtrar(p):
    return p['preco'] >100

novos_produtos_ = filter(
    filtrar,
    produtos
)


print_iter(novos_produtos)
print_iter(novos_produtos_)
print_iter(produtos)