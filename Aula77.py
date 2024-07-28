# Manipulando chaves e valores em dicionários

# criando uma chave:
#   primeiro eu crio um dicionario vazio

pessoa = {}


pessoa['nome'] = 'Elias' #A chave fica dentro dos colchetes e o valor é atribuido fora

print(pessoa)
print (pessoa['nome']) #acessando a chave normalmente

# print(pessoa['nome1'])#Acessando uma chave inesistente dara um KeyError: 'nome1'


# se for uma lista vazia dara um IndexError: list index out of range

# funcionario=[]
# print(funcionario[0])

# ============== CHAVES DINAMICAS =================

chave = 'nome'
pessoa[chave] = 'Joao'

print(pessoa[chave]) #a chave foi atribuida em uma variável que posso manipular dinamicamente

# APAGANDO UMA CHAVE
pessoa['sobrenome'] = 'Miranda'
print(pessoa)

del pessoa['sobrenome'] #Aqui deleto a chave
print(pessoa)


#ACESSANDO VARIAVEIS Q NAO EXISTE ,TENTAR OBTER A CHAVE
print(pessoa.get('sobrenome', 'Não existe')) #o get procura a chave no dicionario e traz a proxima opçao se n existir

print(pessoa.get('sobrenome'))# se eu n colocar nada pra substituir ele traz None=vazio

#procurando pelo if

if pessoa.get('sobrenome') is None:
    print('Chave n existe')
else:
    print(pessoa['sobrenome'])