"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print(
        '█▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█   █ █▄░█ ▀█▀ █▀▀ █ █▀█ █▀█',
        '█░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█   █ █░▀█ ░█░ ██▄ █ █▀▄ █▄█',sep='\n')


numero = input('Digite um número inteiro qualquer:...')

try:
    numero_int = int(numero)
    if numero_int%2==0:
        print(f'O numero {numero} é inteiro e par')
    else:
        print(f'O número {numero} é inteiro e ímpar')

except:
    print(f'Você não digitou um numero inteiro!')



print(
'█▀▀ █▀▀█ █──█ █▀▀▄ █▀▀█ █▀▀ █▀▀█ █▀▀█',
'▀▀█ █▄▄█ █──█ █──█ █▄▄█ █── █▄▄█ █──█',
'▀▀▀ ▀──▀ ─▀▀▀ ▀▀▀─ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀▀',sep='\n')


hora = input('Por Favor, me informe o horário no formato de 24hrs:..')

hora_int = int(hora)
try:
    if hora_int >4 and hora_int<13:
        print('Bom Dia !')
    elif hora_int >12 and hora_int<18:
        print('Boa Tarde !')
    else:
        print('Boa Noite')
except:
    print('Você não informou um horario')



print(
'███╗░░██╗░█████╗░███╗░░░███╗███████╗',
'████╗░██║██╔══██╗████╗░████║██╔════╝',
'██╔██╗██║██║░░██║██╔████╔██║█████╗░░',
'██║╚████║██║░░██║██║╚██╔╝██║██╔══╝░░',
'██║░╚███║╚█████╔╝██║░╚═╝░██║███████╗',
'╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝',sep='\n')

nome = input('Digite seu primeiro nome:...')

if len(nome) <=4:
    print(f'Seu nome {nome} é curto e tem {len(nome)} letras')
elif len(nome) >4 and len(nome) <=6:
    print(f'Seu nome {nome} é médio e tem {len(nome)} letras')
else:
    print(f'Seu nome {nome} é grande e tem {len(nome)} letras')