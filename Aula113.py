# REDUCE - Faz a reducao de um iteravel em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def funcao_interna_reduce(acumulador, produto) : #essa funcao recebe um acumulador = acumulador e uma iterador produto
    print(f'produto:, {produto['nome']} | {acumulador}')
    print('')
    return round(produto['preco']+acumulador,2)


total = reduce(
    funcao_interna_reduce,
    produtos,
    0
)#para utilizar o reduce precisamos de uma funcao 'auxiliar'

print(total)