"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y, z=3):
    #definicao
    print(f'{x=}, {y=}', '|' , '(x + y)*3', (x+y)*z)

soma(10, 15
     )