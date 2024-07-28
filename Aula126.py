# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'Joao', 'idade': 35}
p1 = Pessoa('Joao', 35)
p2 = Pessoa(**dados)
# p1.nome = 'Errado'
print(p1.__dict__) #consigo ver os dados de p1, um dicionario onde os dados estão

p1.__dict__['outra']='coisa'
# no __dict__ eu consigo criar mais instancias dentro da variavel


print(vars(p1)) #vars chama o __dict__ da variavel

print(vars(p2))

