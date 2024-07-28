'''
Imprecisão de ponto flutuante



'''
import decimal

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2

print (numero3)
print (f'{numero3:.2f}') # formatando o resultado // retorna uma string

print (round(numero3,1)) #aqui retorna um float

#usando o modulo decimal

numero1 = decimal.Decimal(numero3) # é ideal para numeros de ponto flutuante muito grandes
print (numero1)