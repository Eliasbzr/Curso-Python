
def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


#TRANSFORMANDO A FUNCAO SOMA EM LAMBDA

print(
    executa(lambda x,y: x+y,
            2, 7
            ) #funcoes lambda n tem nome, parenteses ou usam return para o valor
)

#TRANSFORMANDO A FUNCAO cria_multiplicador em LAMBDA:
#lambda n é idicado para codigos assim:

duplica = executa(lambda m: lambda n: n*m,2)
print(duplica(10))

#lambda tbm aceita args
