# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


#Criando um erro, 
#A necessidade de se criar um erro dentro de um programa
# é para o desenvolvedor se comunicar com os demais 
# e facilitar a identificação do erro que o programa apresenta


class MyError(Exception): #para seguir a convencao do python td erro deve ser identado com o sufixo Error
    ...

class Outroerro(Exception):
    pass

def levantar():
    exception_ =MyError('Outra Mensagem', 'b', 'c')
    exception_.add_note('Erro nesta linha 26') #adicionando notas de erro
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exeption_ = Outroerro('Relancando erro')
    raise exeption_ from error