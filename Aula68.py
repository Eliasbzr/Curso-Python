"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos 
externos
A palavra global faz uma variável do escopo externo 
ser a mesma no escopo interno.
"""


#MA PRATICA USAR O GLOBAL COMO ESTA NAS FUNCOES



def escopo():
    x = 1
    print (x)

#print (x) #não da pra chamar o x fora da função | td dentro da funcao so executa ela

def escopo2 ():
    print (x)

x = 12 #Usando o valor fora da função |




x = 55

def escopo3():
    global x 
    x=37

    def funcao_interna():
        global x
        x=46
        y=14
        print(f'Imprimindo X e Y da Funcao mais interna {x}, {y}')

    funcao_interna()
    print (f'Imprimindo o X da funcao externa {x}')


print (f'Imprimindo o X fora do escopo {x}')

escopo3()




