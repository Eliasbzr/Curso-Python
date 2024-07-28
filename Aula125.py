# Atributos de Classe

class Pessoa:
    ano_atual = 2024 #isso é um atributo de classe, 
                    # ele funciona dentro de toda classe
                    # e para todas as instancias que criarmos


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #chamar o atributo com o nome da classe
    


p1 = Pessoa('Joao,', 40)
p2 = Pessoa('Helena',4)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
