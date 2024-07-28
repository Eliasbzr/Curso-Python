'''
Siplit e join com list e str
split-> divide uma string
join -> une uma string

'''

frase = '    Olha que coisa    ,     interessante    '

lista_palavras = frase.split(' ') #Dividindo pelo espaço
lista_palavras = frase.split(',') #Divide na lista

print (lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip()) #O modulo strip corta os espaços do inicio e do fim
                                     #lstrip corta somente o espaco da esquerda
                                     #rstrip corta somente o espaco da direita
#arrumando os espacos extrar

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()  # não é recomendado corrir as listas

print (lista_palavras)

#é por convensão não alterar listas, mesmo estando erro,
# o ideal é criar uma nova lista arrumada.

#/ UTILIZANDO O JOIN  /
frases_unidas = '-'.join(lista_palavras) #unindo das listas pelo separador '-', primeiro é passado o separador
print(frases_unidas)