'''
GERANDO UM CPF ALEATÓRIO

'''
import random as rd

voltas = range (1,11)

for volta in voltas:

   
    cpf_corpo = ''

    for digito in range(9):
        cpf_corpo += str(rd.randint(0,9))
       
    dig1 = 0
    dig2 = 0
    seq_multiplicador = 10

    for numero in cpf_corpo:
        dig1 = dig1 + (int(numero)*seq_multiplicador)
        seq_multiplicador -=1
    dig1 = 0 if ((dig1*10)%11) >9 else ((dig1*10)%11)

    numero = 0
    seq_multiplicador = 11

    cpf_10 = (str(cpf_corpo) + str(dig1))
    for numero in cpf_10:
        dig2 = dig2 + (int(numero)*seq_multiplicador)
        seq_multiplicador -=1
    dig2 = 0 if ((dig2*10)%11) >9 else ((dig2*10)%11)
    #print (f'Corpo: {cpf_corpo} | dig1: {dig1} | dig2 : {dig2} | CPF Completo: {(str(cpf_corpo) + str(dig1) + str(dig2))}')
    print ((str(cpf_corpo) + str(dig1) + str(dig2)))

