# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor*porcentagem,2)

aumentar_10_porcento = partial(
    aumentar_porcentagem, 
    porcentagem = 1.1) #nomeando o argumento da unção acima
# um partial é como se fosse uma closure, uma função que tem outra funcao dentro

# novos_produtos = [
#     {**p, 'preco': aumentar_10_porcento(p['preco'])}
#     for p in produtos
# ]

# for p in novos_produtos:
#     print(p, sep='\n')

def muda_preco_produtos(produto):
    return {
        **produto,
        'preco':aumentar_10_porcento(
            produto['preco']
            )
    }

novos_produtos = map( #o map vai passar a funcao em cada produto
    muda_preco_produtos,
    produtos

)
for p in novos_produtos:
    print(p, sep='\n')