"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os



print (
'███████╗░█████╗░██████╗░░█████╗░░█████╗░',
'██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗',
'█████╗░░██║░░██║██████╔╝██║░░╚═╝███████║',
'██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══██║',
'██║░░░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║',
'╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝',sep='\n')

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
tentativas_total = 10


while True:
    while tentativas <= tentativas_total:
        letra_digitada = input('Digite uma letra:... ')
        tentativas +=1
        
        if len(letra_digitada) >1:
            print('Digite apenas uma letra. ')
            continue

        if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada +=letra_secreta
            else:
                palavra_formada +='*'
        print (f'Você ainda tem {int(tentativas_total) - int(tentativas)} tentativas')
        print(f'Palavra formada: {palavra_formada}')
        if tentativas == tentativas_total:
            print ('Você perdeu')
            quit()
        if palavra_formada==palavra_secreta:
            os.system('cls')
            print ('VOCÊ GANHOU 🏆')
            print ('')
            print(f'você utilizou {tentativas} tentativas')
            palavra_formada =''
            letras_acertadas = ''
            tentativas = 0

        