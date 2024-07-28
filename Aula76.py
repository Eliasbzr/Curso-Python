
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')


''' 

Dicionarios sao chave e valor - sao sempre pares de chave e valor - funcionam como indice

UTILIZAMOS DICIONARIOS PARA COISA COM ATRIBUTOS, COMO POR EXEMPLO:
    PESSOAS
    PRODUTOS
    

'''
#ESSA É A FORMA MAIS COMUM DE SER UTILIZADO

pessoa = {'nome': 'Elias',
          'sobrenome': 'Bezerra da Silva',
          'idade': 32,
          'altura':1.76,
          'endereco': [
              {'rua':'Carolina', 'numero':331},
              {'rua':'Dos Bobos', 'numero': 0}
          ],

}
# print (pessoa, type(pessoa)) #<class dict>

# # Acessando o valor do dicionário

# print(pessoa['nome']) #basta colocar os colchetes que o vs code ja coloca os valores que tem no dict
# print (pessoa['sobrenome'])

#Consigo colocar um for no dicionario para ver as chaves

# for chave in pessoa:
#     print (chave)

#TBM é possivel acessar o dicionario completo com o for
for chave in pessoa:
    print(chave, pessoa[chave])




# ============================  OUTRA FORMA DE CRIAR UM dict ====================================
# ESSA FORMA NAO É MUITO COMUM DE SER UTILIZADO

# pessoa_2 = dict() 
# print (pessoa_2, type(pessoa_2)) #<class dict>

# #atribuindo chave e valor:
# pessoa_2 = dict(nome='Elias', sobrenome = 'Bezerra da Silva') #assim funciona o = / lista com chaves n funciona tem q ser : para atribuir valor
# print (pessoa_2, type(pessoa_2)) #<class dict>

#=====================================================================================================
