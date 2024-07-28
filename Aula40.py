''' Calculadora com While '''
print (
'░█████╗░░█████╗░██╗░░░░░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░',
'██╔══██╗██╔══██╗██║░░░░░██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗',
'██║░░╚═╝███████║██║░░░░░██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║',
'██║░░██╗██╔══██║██║░░░░░██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║',
'╚█████╔╝██║░░██║███████╗╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║',
'░╚════╝░╚═╝░░╚═╝╚══════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝',sep='\n')



while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+ - * /): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0 

    try:
       num_1_float = float(numero_1)
       num_2_float = float(numero_2)
       numeros_validos = True
    except:
       numeros_validos  = None
   
    if numeros_validos is None:
        print ('Você não digitou um numero valido')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ('Você não digitou um operador valido')
        continue

    if len(operador) > 1:
        print ('Digite apenas um operador valido')
        continue   
    print('Realizando operação, confira seu resultado: ')
    if operador == '+':
        print(num_1_float+num_2_float)
    elif operador =='-':
         print(num_1_float-num_2_float)
    elif operador =='/':
         print(num_1_float/num_2_float)
    elif operador == '*':
         print(num_1_float*num_2_float)
    else:
        print('nunca ira chegar aqui')
    

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print('Você saiu !')
        break
