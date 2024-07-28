# Herança simples - Relações entre classes
# Associação - um objeto usa outro objeto e eles existem separadamente, Ex: class escritor, class caneta => um escritor usa caneta 
# Agregação - um objeto TEM outro objeto, outro objeto é parte daquele objeto, ex class carrinho, class arroz => No carrinho de compras TEM um arroz
# # Composição - um objeto É dono de outro objeto, Herança  Ex class pessoa class cliente, toda pessoa é um cliente, a class pessoa
# generaliza o cliente, portanto a class cliente pode herdar os atributos da classe pessoa, bem como a class pessoa pode ser derivada
# em class aluno, class homem, class mulher e etc.

# Quanto mais avancam as relacoes, mais fortes elas ficam
# ou seja:
#                       =======ASSOCIAÇÃO=======
#                       | =====agrecação=====   |
#                       | |   ==herança==    |  |
#                       | |   |==========|   |  |
#                       | |==================|  |
#                       |=======================|
# 
# 
# 
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class, classe pai

#       a classe pai da como herança tds os metodos atributos, e etc para as classes filhas
#       logo eu n preciso criar outro metodo dentro da classe filha q faca a mesma coisa
#       q a classe pai faz, pq a classe filha é do tipo da classe pai portando ela tem acesso a tds
#       os metodos da classe pai

# Classes filhas (Cliente)
#   -> sub class, child class, derived class, classe filha


# TODO CLIENTE É UMA PESSOA





