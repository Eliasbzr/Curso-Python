'''
Enumerate - enumera iteráveis (indices)

'''
#[(0, 'Maria'), (1, 'Joao'), (2, 'Marcelo'), (3, 'Elias')]
lista = ['Maria', 'Joao', 'Marcelo']
lista.append('Elias')

lista_enumerada = enumerate(lista) # esse iterator so pode ser utilizado uma vez
print(next(lista_enumerada)) #pegando o 1 valor da lista  -printa a tupla

for item in lista_enumerada:
    print (item) #Mostrando todos os itens da lista -- printa tupla por tupla


#para utilizar varias vezes o enumerate devemos coloca-lo direto no for
    print('Iterator varias vezes')

for item in enumerate(lista):
    print (item) #Mostrando todos os itens da lista -- printa tupla por tupla


for item in enumerate(lista):
    print (item) #Mostrando todos os itens da lista -- printa tupla por tupla

print('Varialvel lista')
#tbm podemos fazer convertendo o enumerate em uma lista
lista_enum = list(enumerate(lista))
print(lista_enum)

#acessando diretamente a variavel:
print ("For ja separando as variaveis")
for indice, nome in enumerate(lista):
    print (indice, nome)