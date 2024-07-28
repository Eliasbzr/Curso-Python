# Funções decoradoras e decoradores com classes
def adiciona_repr(cls):
    def meu_repr(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr #essa definicao para o repr pra dentro da classe
    return cls

# PARA USAR COMO HERANCA DENTRO DA CLASSE
# class MyReprMixin:
#     def __repr__(self) -> str:
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

@adiciona_repr #DESSA FORMA ESTOU PASSANDO A FUNCAO PRA DENTRO DA CLASSE
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr #DESSA FORMA ESTOU PASSANDO A FUNCAO PRA DENTRO DA CLASSE
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# Time(adiciona_repr(Time)) #ESTOU PASSANDO O ADCIONA REPR PRA DENTRO DA CLASSE SOBREESCREVENDO-A // NAO É UMA FORMA TAO USUAL
# Planeta(adiciona_repr(Planeta)) ## ''



brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)