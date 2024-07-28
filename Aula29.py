'''Introdução ao try/except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

'''

print(1234)
print(5678)
#int('a')

numero= input('Dobrando o numero:...')

try: #tenta executar td o q esta dentro do try,
     #caso tenha erro vai para o except
    numero_flt = float(numero)
    print('Float: ', numero_flt)
    print(f'O numero dobrado é {numero_flt*2}')
except:
    print('Isso não é um número !')