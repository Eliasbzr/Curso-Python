'''
Exercício
Exiba os indices da lista

'''

lista = ['Maria', 'Joao', 'Pedro', 'Marcela']
lista.append('Ana')
lista[1] = 'Elias'
indice = 0

for nome in lista:
    print (f'{indice} - {nome}')
    indice +=1

#=========================
# outra forma de resolver usando range

lista = ['Maria', 'Joao', 'Pedro', 'Marcela']
indices = range(len(lista))

for numero in indices:
    print (numero, lista[numero])