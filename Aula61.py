"""
Calculo do primeiro dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

'''
CALCULANDO O PRIMEIRO DIGITO DE UM CPF 

'''
import re
import sys

while True:
    resultado = 0
    contador_regressivo_1 = 10
    
    cpf_completo = input('Digite seu CPF:...')
    cpf_informado = re.sub(r'[^0-9]','',cpf_completo) #o modulo re substiui tudo o q n for numero

    cpf_sequencial = cpf_informado == cpf_informado[0]*len(cpf_informado)

    if cpf_sequencial:
        print('Você digitou um numero sequencial')
        sys.exit()

    cpf_corpo = cpf_informado[:9]
    cpf_ctrl = cpf_informado[-2:]
    cpf_dig1 =int(cpf_ctrl[:1])
    cpf_dig2 =int(cpf_ctrl[-1:])
    
    for numero in cpf_corpo:
        resultado += int(numero) * contador_regressivo_1
        contador_regressivo_1-=1
    resultado = ((resultado*10)%11)
    dig1_cpf = 0 if resultado >9 else resultado

    '''
    verificando o 2 digito
    FORMULA: cpf_corpo e dig1_cpf
    MULTIPLICANDO OS 10 DIGITOS EM UMA CONTAGEM REGRESSIVA DE 11
    '''
    resultado2 = 0
    contador_regressivo_2 = 11
    str_cpf_corpo_dig1 = (str(cpf_corpo)) + (str(dig1_cpf))
    for digito in str_cpf_corpo_dig1:
        resultado2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -=1
    
    resultado2 = ((resultado2*10)%11)
    dig2_cpf = 0 if resultado2 >9 else int(resultado2)

    '''
    RESULTADO FINAL 

    '''
    if cpf_dig1 == int(dig1_cpf) and cpf_dig2 == int(dig2_cpf):
        print ('Cpf Validado 😁')
    else:
        print ('CPF Inválido 😭! ')
