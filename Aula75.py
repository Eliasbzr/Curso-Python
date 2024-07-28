'''
Crie uma funcao que duplique, tripique e quadruplicam
o numero recebido como parametro

'''


def multiplicador (multiplicador):
    def multiplicar (numero):
        return numero*multiplicador
    return multiplicar



duplicar = (multiplicador(2))

triplicar = (multiplicador(3))
        
quadruplicar = (multiplicador(4))   



print(duplicar(2))
print(triplicar(2))
print (quadruplicar(2))
