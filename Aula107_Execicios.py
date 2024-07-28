# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados =  ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1),len(lista2))

    return[
       (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]

from itertools import zip_longest

print(list(zip(cidades, estados))) #a funcao zip faz exatamente a mesma coisa
                                   #iterando pela menor lista
                                   
print(list(zip_longest(cidades, estados, fillvalue='Sem Valor'))) #zip_longest itera sobre a maior lista
                                                                  # fillvallue preenche os zerados
print(zipper(cidades,estados))

