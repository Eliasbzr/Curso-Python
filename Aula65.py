"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


#Definindo uma função

#Estrutura

def exemplo_funcao():                               #nome da funcao, sempre minusculo e underline qdo houver espaco
    print('Processamento de código')                #processamento da função, td o que ela vai executar


exemplo_funcao()                                    #chamando a funcao

#passando parametros para funcao

def imprimir(a, b, c): #parametros sao qdo eu escrevo defino a funcao
    print (f'Parametro a: {a}')
    print (f'Parametro b: {b}')
    print (f'Parametro c: {c}')

imprimir('oi','ola', 'Hello') #argumentos são os valores q coloco qdo utilizo a funcao

#Não passando valor para funcao
def saudacao (nome='Não informado'): #o 'Nao informado ja vem default, sera trocado caso eu informe a variavel
    print(f'Olá {nome}')

saudacao('Elias')
saudacao('Maria')
saudacao ()



def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)