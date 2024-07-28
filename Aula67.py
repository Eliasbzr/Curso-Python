"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma (x, y):
    print (f'Soma de {x=} + {y=} = ',x+y)


#Funcao para verificar se um parametro foi enviado ou nao:

def soma (x, y, z=None): #setando a variavel z vazia | todos os parametros apos o parametro com valor precisam ser setados com valor 
    if z is None:
        print (f'{x=} | {y=} | soma de x + y =', x+y)
    else:
        print (f'{x=} | {y=} | {z=} | Soma de x+y+z =', x+y+z)


soma(1,3)
soma(1,1,5)