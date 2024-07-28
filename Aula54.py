'''
Faça uma lista de compras com listar
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista

Não permita que o programa quebra com erros de indices inexistentes na lista


'''

'''
Selecione uma opção:
[i]serir [a]pagar [l]istar: 
'''
import os

compras = []

while True:
    print (
'██╗░░░░░██╗░██████╗████████╗░█████╗░  ██████╗░███████╗',
'██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝',
'██║░░░░░██║╚█████╗░░░░██║░░░███████║  ██║░░██║█████╗░░',
'██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░',
'███████╗██║██████╔╝░░░██║░░░██║░░██║  ██████╔╝███████╗',
'╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝',
'',
'░█████╗░░█████╗░███╗░░░███╗██████╗░██████╗░░█████╗░░██████╗',
'██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝',
'██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██████╔╝███████║╚█████╗░',
'██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██╔══██╗██╔══██║░╚═══██╗',
'╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║██║░░██║██████╔╝',
'░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░', sep= '\n')
    opcao = input ('Selecione uma opção: \n'
                '[i]serir [a]pagar [l]istar: ')

    if opcao.lower() == 'i':
        os.system('clear')
        item = input ('Insira o produto na lista: ')
        compras.append(item)


    elif opcao.lower() == 'a':
        remover_str = input ('Digite o indice a ser removido: ')

        try:
            remover = int(remover_str)
            del compras[remover]
            print ('Item Removido')
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:  #é possivel utilizar mais de um except dentro do try e listar qual o tipo de erro
            print ('Digite um numero dentro da lista')
        except Exception:
            print ('Erro desconhecido')


    elif opcao.lower() == 'l':
        os.system('clear')
        if len(compras) ==0:
            print ("Nada para listar")
        else: 
            for indice, produto in enumerate(compras):
                print (indice, produto)


    else:
        print ('Voce n digitou uma opcao valida')
    continue
    

'''
last = numeros[1]
numeros.pop(1)
print (f'removendo da lista {last}')
print (numeros) #tbm posso remover passando o indice, é indicado fazer apenas em listas pequenas
'''