# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

nota_maxima = 3
respostas_acertadas = 0

for pergunta in perguntas:
        print('Questão: ',pergunta['Pergunta'])
        print('')

        print('Opções:')
        for numero, opcao in enumerate(pergunta['Opções']):
                print(f'{numero})', opcao)
        print ('')

        resposta_recebida = None

        input_resposta_recebida = (input('Digite o indice da resposta:...'))
        resposta = pergunta['Resposta']
       
        
        if input_resposta_recebida.isdigit():
             resposta_recebida = int(input_resposta_recebida)

    
        try:
            resposta_recebida = (pergunta['Opções'][input_resposta_recebida])
        except IndexError:
            print('Digite um valor dentro da lista')
            continue

        if resposta == resposta_recebida:
            print('Parabens ! você acertou 🏆')
            print('')
            respostas_acertadas +=1
        else:
            print ('Que pena você errou ❌')
            print ("")

if respostas_acertadas == nota_maxima:
     print ('Parabéns !!!! \nVocê acertou todas as respostas 🥇 ')
elif respostas_acertadas == 2:
     print ('Você acertou 2 respostas 🥈')
elif respostas_acertadas ==1:
     print('Você acertou 1 resposta 😢')
else:
     print('Você errou todas as questões 👹')
    


    