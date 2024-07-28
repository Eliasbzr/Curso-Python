print(      
'███████████████████████████████',
'█▄─█▀▀▀█─▄█─█─█▄─▄█▄─▄███▄─▄▄─█',
'██─█─█─█─██─▄─██─███─██▀██─▄█▀█',
'▀▀▄▄▄▀▄▄▄▀▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀',sep='\n')

''' Estrura de repeticao WHILE '''
'''
condicao = True

# loop infinito
while condicao:
    nome=input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome =='sair':
        break
'''

    # break: o break busca o while mais proximo

    # A condicao dentro do while esta 'uncheable' ou seja inalcancavel
while False:
        print('Eita')

contador = 0

while contador <= 10:
        print(contador)
        contador = contador + 1
