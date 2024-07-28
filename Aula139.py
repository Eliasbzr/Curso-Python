# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
#as classes criadas em python ja herdam tds as funcoes do método object

# automaticamente as classes herdam os modulos de object, mas se quisermos que a classe herde de outro basta colocar
# nos parenteses
class Foo(object): #deixando explicito que essa classe herda de object, mas poderia ser de qualquer outra
    pass

# ESSA É A SUPER CLASSE
class Pessoa ():
    cpf = 1634 #atributo de classe
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print(f' {self.nome}, {self.sobrenome}, = {self.__class__.__name__}')
    #em ambas as classes herdam o metodo da super classe


class Cliente(Pessoa): #com a classe pessoa dentro dos parenteses a classe cliente esta herdando tudo da classe pessoa
    pass



class Aluno(Pessoa):
    pass

c1 = Cliente('Elias', 'Bezerra')
a1 = Aluno(sobrenome='Silva', nome='Joao')
c1.cpf = 4005

c1.falar_nome()
a1.falar_nome()

print(a1.cpf)
print(c1.cpf)

