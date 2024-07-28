"""
Desempacotamento em chamadas
de metodos e funcoes


"""

string = 'ABCD'
lista = ['Maria', 'Joao', 'Helena','Henrique', 'Bruna']
tupla = 'Python', 'é', 'legal'
salas = [['Amanda', 'Bruna', 'Carlos', 'Daniel'],
         ['Andre', 'Barbara', 'Carol'],
         ['Ana', 'Diego', 'Elias']]

#desempacotando itens aleatórios

p, *_, u = lista
print(f'1º {p}| Ultimo {u}') #pegando o 1 e ultimo da lista

p, *_, pn, u = lista
print(f'1º: {p}| Penultimo: {pn}  | Último: {u}') #pegando o 1º penultimo e ultimo da lista

p, *_, pn, u = lista
print (*_)


for letra in string:
    print (letra)

print(*string, sep='\n') #DESEMPACOTANDO DIRETO NO PRINT

print(*salas, sep='\n')