'''

args - Argumentos nao nomeados
* - *args (empacotamento e desempacotamento)


'''
#Lembrete de desempacotamento

x, y, *resto = 1,2,3,4
print (x, y, resto)

def soma(x, y):
    return x+y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return (total)


fatoracao = soma(1,2,3,4,5,6)
print (f'Fatorando os numeros: {fatoracao}')

#DESEMPACOTANDO VARIVEL

numeros = 1,2,3,4,5,6,7,8,9
#outra_soma = soma(numeros)  NÃO DA PARA UTILIZAR UMA TUPLA DENTRO DE UMA FUNCAO QUE PEDE ARGUMENTOS, ACABA FICANDO UMA TUPLA DENTRO DA OUTRA
outra_soma = soma(*numeros) #assim desempacota
print (outra_soma)

