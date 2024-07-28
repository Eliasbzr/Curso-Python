'''
DADOS MUTAVEIS
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memória (mutavel)
'''

lista_a = ['Luiz', 'Maria']
lista_b = lista_a # -> referencio a lista a,'/
                        #entao qdo ocorrer alteração na lista a se refletira na lista b
print (lista_b) #-> lista b ainda é um objeto lista

lista_b.append('Joao') # -> alterar a lista b tbm altera a lista a

lista_a.append('Elias') #-> Alteração aparece nas duas variaveis
print(lista_a)
print(lista_b)

#para criar realmente uma segunda lista basta usar o metodo copy

lista_b = lista_a.copy()
lista_b.append('Maria') #apendou apenas na lista b pq as 2 variaveis agr
                        #apontam para lugares diferentes na memoria

print(lista_b)


#==================================================================================
# UTILIZANDO FOR EM LISTAS

'''
for in com listas

'''
lista = ['Maria', 'Joao', 'Luiz']

for nome in lista:
    print (f'* {nome}')
'''Acessamos os valores dentro da lista, o for percorre todos os itens
   dentro da lista
'''
