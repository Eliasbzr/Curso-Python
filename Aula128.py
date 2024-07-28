# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# DECORANDO UM MÉTODO COM O @classmethod
    @classmethod #classmethod faz com que eu possa chamar a minha classe sem passar o self, recebendo a propria classe 'cls'
    def metodo_de_classe(cls):
        print('Hey')

# ESTAMOS CRIANDO UM 'PADRAO' DE CRIAR PESSOAS DENTRO DA CLASSE MAS SEM ALTERAR O DEFAULT DA CLASSE
    @classmethod #classmethod faz com que eu possa chamar a minha classe sem passar o self, recebendo a propria classe 'cls'
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

   
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anonimo', idade)


    

p1 = Pessoa(nome='Elias', idade=32)
Pessoa.metodo_de_classe()

p2=Pessoa.criar_com_50_anos('Ana')
p3 = Pessoa.criar_anonimo(22)

print(p2.__dict__)
print(p3.nome, p3.idade)
