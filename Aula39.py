'''
Iterando strings com while

'''
#colocar um * em cada letra dentro da string = *E*l*i*a*s *B*e*z*e*r*r*a


nome = 'Elias Bezerra'

novo_nome = ''

inicio = 0
fim = len(nome)

while inicio <fim:

    novo_nome = novo_nome+(f'*{nome[inicio]}')

    inicio += 1

print (novo_nome)
