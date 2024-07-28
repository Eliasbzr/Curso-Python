#LIST COMPREHENSION 
#É uma forma rápida para criar listas a partir de iteráveis

#conhecemos 2 formas de criar listas:
# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)

# #agr utilizando o list comprehension

# lista = [numero for numero in range(10)] #Posso utilizar o for para incluir os
#                                          #numeros dentro da lista, desde que 
#                                          #a esquerda do for eu inclua o valor 
#                                          #a ser adicionado na lista
# print(lista)

# lista_repetida = ['!' for numero in range(5)] #é adicionado 5x o !
# print (lista_repetida)

# #tbm posso fazer operações:
# operacao = [
#     numero * 2 #posso fazer varias operações aqui dentro
#     for numero in range(10) #é como se fosse um for ao contrário
# ]
# print (operacao)

#MAPEAMENTO DE DADOS COM LIST COMPREHENSION

# produtos = [
#     {'nome' : 'p1', 'preco': 20,},
#     {'nome': 'p2' , 'preco' : 10,},
#     {'nome': 'p3', 'preco': 30,},
# ]

# novos_produtos = [
#    {'nome ': produto['nome'], 'preco ': (produto['preco']*1.1)} #refazendo o dicionário
#                                                                 #e adicionando alteracoes
#     for produto in produtos
# ]
# #TBM POSSO FAZER ALTERAÇÕES DE UMA VEZ


# novos_produtos = [
#     {**produto, 'preco': produto['preco']*1.15} 
#     #o ** desempacota todos os produtos
#     for produto in produtos
# ]

# #Aumentando o preço do produto caso ele for acima de 20
# novos_produtos = [
#     {**produto, 'preco' : produto['preco'] * 1.15}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# # print (novos_produtos)
# print (*novos_produtos, sep='\n')

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
#uma forma mais amigavel para printar valores



#FILTRANDO DADOS 

produtos = [
    {'nome' : 'p1', 'preco': 20,},
    {'nome': 'p2' , 'preco' : 10,},
    {'nome': 'p3', 'preco': 30,},
]

produtos_filtrando = [
    {**produto}
    for produto in produtos 
    if produto['preco'] > 20 #para filtrar o if vem depois do for 
                             # e não precisa de elseEE

]  

p (produtos_filtrando)