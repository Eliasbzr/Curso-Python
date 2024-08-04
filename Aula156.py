# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)
class Meta(type):
    def __new__(msc, name, bases, dct):
        print('Metaclass de new')
        cls = super().__new__(msc, name, bases, dct)
        cls.attr = 'atributo de metaclasse'
        return cls
    
    # a classe meta é uma metaclasse ela ja existe automaticamente no python 
    # toda classe herda de metaclasse
    # toda classe é uma instancia de metaclass


class Pessoa(metaclass=Meta): #a classe pessoa esta herdando de meta que é uma metaclasse que so foi criada para explicar como
                            #   o python trabalha
    def __new__(cls, *agrs, **kwargs):
       print("MEU NEW")
       instancia = super().__new__(cls)
       return instancia
    
    def __init__(self, nome):
        print('Meu init')
        self.nome = nome

# p1 = Pessoa('Elias')
# print(p1.nome)
print (Pessoa.attr)