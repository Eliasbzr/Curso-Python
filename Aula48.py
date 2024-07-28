'''
LISTAS

Tipo list -> Mutavel 
suporta valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos uteis: append, insert, pop, clear, extend

na lista conseguimos:
CRUD
CREATE  READ    UPDATE      DELETE
CRIAR   LER     ATUALIZAR   DELETAR

'''

string = 'ABCDE' #5 caracteres

lista = [] #lista é criada por colchetes
lista = [123, 'Elias bezerra', True, 1.5, []] #lista suporta td ao mesmo tempo inclusive outra lista dentro
print (lista)

#..................
#para acessar os itens da lista
print (lista[1].upper())

#--------------------
#atribuindo valor na lista
lista[1] = 'Cachorro'
print (lista)

numeros= [10,20,30,40]
print(numeros)

#..............
#ADICIONANDO NA LISTA
numeros.append(50)
print (f'apendando na lista {numeros[-1]}')
print(numeros)

#REMOVENDO DA LISTA
last = numeros[-1]
numeros.pop() #remove o ultimo valor
print (f'Removendo da lista {last}')
print(numeros)

last = numeros[1]
numeros.pop(1)
print (f'removendo da lista {last}')
print (numeros) #tbm posso remover passando o indice, é indicado fazer apenas em listas pequenas

#--------------
#limpando a lista
lista = [10,20,30,40]
lista.clear()
print(lista)


#---------------
#inserindo na lista por posição
lista.insert(0,'Elias') #-> posição inserida e valor inserido
print (lista)


#--------------------
#concatenando listas

lista_a = ['a1,', 'a2','a3']
lista_b = ['b1','b2','b3']
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print (lista_c)
print (lista_d) # n pode ser utilizado como uma variavel, pq a lista a é q foi mexida
print (lista_a)