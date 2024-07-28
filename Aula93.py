# Try, except, else e finaly

try:     
# try esta sempre acompanhado do except, try n funciona sozinho
    ...
except():
#boa pratica o erro do except deve ser explicito
    ...


# TRATANDO ERRO EXPLICITO
try:
    a = 18/2
    print(a)

#posso tratar erro por erro com varios except, ou colocar dentro do parenteses
#para os erros q n especifiquei usamos o Exception
except(ZeroDivisionError):
    print('Divisao por zero')
except(NameError):
    print('Erro de variavel')
except(Exception):
#nesta linha trata os demais erros q não informei

    print('Erro desconhecido')

#PEGANDO O NOME E CLASSE DO ERRO
linha1 = range(10)
try:
    a=10/0
    print(a)
except ZeroDivisionError as error:
    print(error) #imprime a msg de rro
    print(error.__class__.__name__)    #imprime a classe do erro

