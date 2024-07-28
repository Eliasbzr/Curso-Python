'''
Exercicios

Crie uma funcao que multiplica todos os argumentos 
nao nomeados recebidos

retorne o total para uma variavel e mostre o valor


Crie uma funçao que identifica um numero par ou impar
#Retorne se o numero e par ou impar
'''
#Multiplicacao

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = print (multiplica(1,2,3,4,5))


def par_impar(a):
    div = int(a)%2
    if div == 0:
        return (f'O número {a} é par!') ## se for par o cod para aqui, pq qd o cod encontra o return ele finaliza
   
    return (f'O número {a} é impar !') ## caso for impar ele vem pra cá e retorna o resultado


print(par_impar(2))    
print(par_impar(3))    
print(par_impar(20))    
print(par_impar(21))    
