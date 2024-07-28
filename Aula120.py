# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# PascalCase = primeira letra da palavra em maiuscula ex:
# CriarBaseDeDados

# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# UMA CLASSE É UM METODO PARA GERAR INSTANCIAS

class Pessoa:
    def __init__(self,nome, sobrenome): #td metodo se inicia com self q referencia o proprio objeto criado
        self.nome = nome
        self.sobrenome = sobrenome

# Posso colocar atributos dessa forma:

    # p1 = Pessoa('Luiz', 'Otávio')
    # p1.nome = 'Luiz'
    # p1.sobrenome = 'Otávio'
# Não é muito inteligente pois a cada Pessoa nova
# teria de lembrar os atributos todos


p1 = Pessoa('Elias','Bezerra')

print(p1.nome)
print(p1.sobrenome)

