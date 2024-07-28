# dir, hasattr e getattr em Python
# ver quais os metodos estão disponiveis no objeto

string = 'Elias'

if hasattr(string, 'upper'): #checa se a string tem o método
                             # o nome do metodo sempre vem em string tbm ''
    print('Existe método')
    print(string.upper())

# print(string) #usar o debuger na funcao debug console e a funcao dir()

# CHAMANDO O METODO ATRAVES DE UMA VARIÁVEL COM O getattr
# o metodo getattr diz qual o endereco do método

metodo =  'lower' #colocando o metodo que quero verificar dinamicamente
if hasattr (string, metodo):
    print('Existe o lower')
    print(getattr(string, metodo)()) #os parenteses do final executam o metodo