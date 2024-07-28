# raise - lancando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


# para criarmos um erro basta utilizar o modulo raise:

# print(123)
# raise ValueError('Erro de Valor') #1 eu seleciono a classe do erro e dentro dos parenteses eu seto a msg



def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))