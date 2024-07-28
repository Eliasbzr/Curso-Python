#Variaveis Livres + nonlocal (locals, global - para ver se as variaveis sao globais ou locais)

# def fora(x):
#     a = x
#     def dentro():
        
#         return a
#     return dentro


# dentro1 = fora(1)
# dentro2 = fora(50)

# print(dentro1())
# print(dentro2())


def concatenar (str_inicial):
    valor_final = str_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final #com o nonlocal eu armazenei o valor da variavel anterior
        valor_final+=valor_a_concatenar
        return valor_final
    return interna

c = concatenar('Elias') #aqui temos a str_inicial // a variavel c é <class 'function'> q passei o primeiro parametro
                        # e ele esta armazenado na memoria esperando

print(c('Bezerra')) #aqui eu utilizei a função c, passando o parametro interno 'valor_a_concatenar
print(c('da'))
print(c('Silva'))

