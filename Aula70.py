"""
Retorno de valores das funções (return)
"""

def soma_none(x,y):
    print(x+y)
    ##não há retorno nesta função, portando nao é possivel somar o resultado delas em outra variavel
    ## funcoes sem o return a função retorna vazio, o resultado pode ate ser printado, mas não utilizado

#soma_11 = soma_none(1,1)
#soma_22 = soma_none(2,2)

#print (soma_11 + soma_22)



def soma(x, y):
    if x > 10:
        return [10, 20] #Se a condicao for atendida ele retorna e para o codigo
    return x + y  #ja aqui temos o retorno da função
    #APOS O RETURN N É POSSIVELCOLOCAR MAIS PASSOS


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma(11, 55))

