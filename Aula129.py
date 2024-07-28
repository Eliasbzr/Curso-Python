# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def funcao_dentro_da_classe(*args, **kwargs):
        # nao tem acesso a nada dentro da classe
        #tem a o mesmo objetivo de uma funcao de fora da classe
        print("Oi", args, kwargs)

def funcao_de_fora(*args, **kwargs):
    print('oi', args, kwargs)

c1 = Classe()
c1.funcao_dentro_da_classe(1,2,3)

print(funcao_de_fora(vars(c1)))