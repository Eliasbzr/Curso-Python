# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

# print(len(pessoa)) #qtd de chaves no dicionário

# print(pessoa.keys()) #traz as chaves
# print(list(pessoa.keys())) #da pra fazer coercao tbm pra usar como uma lista por exemplo

# print(list(pessoa.values())) #aqui traz os valores ja convertidos com uma lista

# print(list(pessoa.items())) #items traz tudo

# for chave, valor in pessoa.items(): #trazendo chave e valor como no enumerate
#     print(chave, valor) 



# # pegando uma chave que nao existe
# print(pessoa.setdefault('idade')) # se a chave existisse viria o valor

# ==================  Copiando dicionários ==========================

d1 = {
    'c1': 1,
    'c2': 2,
    'l1':[0,1,2]
}

d2 = d1 #não estou criando um novo dicionário, mas apontando a variavel d2 para o mesmo local na memoria

d2['c1'] = 10 #qdo realizo uma alteracao em d2 na vdd o que altera é o d1 q é o dicionário 'original'
print(d1)

d2 = d1.copy #dessa forma criamos realmente um novo dicionário, criando uma copia raza, copiando tudo o q for imutavel
             #tendo um valor mutavel dentro do dicionario, como uma lista por exemplo
             #a 'copia' apontará para o mesmo lugar na memoria.
             #isso e uma shallow copy 

d1['c1'] = 400

print (d1)
print (d2)

#para fazer uma copia profunda, ou seja copiar o dicionário inteiro pra outra variavel temos q utilizar o metodo copy

import copy

d2 = copy.deepcopy(d1)


print(pessoa.get('nome','invalido')) #caso o nome n existe traz o invalido


#apagando chave

nome = pessoa.pop('nome')


#apagando a ultima chave
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

#atualizando o dicionário

pessoa.update({
    'nome':'Elias Bezerra',
    'idade': 32
    }
)

pessoa.update(nome='Elias',idade=32) #outra forma de atualizar o dicionário


#atualizando com uma variavel
tupla = ('nome', 'Erick'), #tem q ter a virgula no final pra ser considerado uma tupla com 1 valor
tp_idade = ('idade',35),

pessoa.update(tupla)
pessoa.update(tp_idade)
print(pessoa)


