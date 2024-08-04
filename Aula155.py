# Metaclasses sao o tipo das classes
# EM PYTHON TUDO É OBJETO (CLASSE TBM)
#Então qual o tipo de uma classe ? (type)
# Seu objeto é um instancia da sua classe
# Sua classe é uma instancia de type (type é uma metaclass)
# type ('Name', (Bases,), __dict__)
# 
# Ao criar uma classe, coisas ocorrempor padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
#  __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (criando a instancia)
#   __init__ da class com os argumentos 
# __call__ da metaclass termina a execução
# 
#  metodos inportantes da metaclass
#  __new__ (msc,name, bases, dct) (cria a classe)
# __call__(cls *args, **kwargs)(cria e inicializa a instancia)
# 
# Metaclasses sao magias mais profundas do que 99% dos usuários 
# deveriam se preocupar. Se você quer saber se precisa delas, 
# não precisa(as pessoas que realmente precisam de uma explicação
# sobre o porquê).
# Tim Peters (CPython core developer)

#objetct acima
class Foo:
    ...
    # herda de object

f = Foo()
# herda da classe foo
print(isinstance(f,Foo))

print(type(f))
print(type(Foo))