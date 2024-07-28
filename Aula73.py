'''
Higher Order Funcition
Funcoes de primeira classe

'''

def saudacao (msg, nome):
    return f'{msg},{nome}!'


def executa(funcao, *args): #*args chama varios argumentos empacotados
    return funcao(*args) #aqui o args esta desempacotando

 
print (executa(saudacao, 'Bom Dia', 'Brasil'))

print (executa(saudacao, 'Boa Tarde', 'Itália'))

#A FUNCAO PODE SER TUDO O Q QUISERMOS
