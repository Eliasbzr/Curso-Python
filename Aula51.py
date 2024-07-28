'''
Introducao ao desempacotamento 
tuplas (tuples)

'''

nomes = ['Maria', 'Joao', 'Pedro', 'Marcela']
nome1, nome2, nome3, nome4 = nomes 
# -> atribui os valores da lista nas variaveis na mesma ordem
# devemos desempacotar todos os itens da lista
print (f'3 nome: {nome3}')

#CAPTURANDO LISTA PARCIAL
nomes = ['Maria', 'Joao', 'Pedro', 'Marcela']
nome, *resto = nomes  # o restante da lista esta armazenado como uma nova lista
                      # na variavel resto, para armazenar basta colocar o 
                      #* na frente do nome

print(f'1 Nome: {nome}')
print(f' lista resto: {type(resto)}')
print (resto)

#caso n for usar a variavel resto, por convenção nomeamos a variavel com _

#PEGANDO UM VALOR FORA DA SEQUENCIA
''' basta colocar a posicao da variavel com o _'''
_, nome2, *_ = nomes
print(f'2 nome: {nome2}')


''' tupla é uma lista imutavel '''

nomes_tupla = 'Maria', 'Joao', 'Pedro', 'Marcela'

print (type(nomes_tupla))

'''nomes_tupla.append #metodo de alteracao nao funciona'''
print(nomes_tupla[2]) #metodos de visualização funcionam

#CONVERTENDO LISTA PARA TUPLA

nomes_tupla2 = tuple(nomes)
print (f'Conversao de lista em tupla {type(nomes_tupla2)}')

#TBM DA PRA CONVERTER TUPLA EM LISTA
nomes_lista2 = list(nomes_tupla2)
print(f' Convertendo lista em tupla: {print(type(nomes_lista2))}')