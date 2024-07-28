
# Herança Múltipla - Python Orientado a Objetos


# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar = existe em a  em b e c, mas nao existe em d
# Problema do diamante
# D herda de B e C // B herda de A // C herda de A
# 
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# 
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)


class A:
    ...

    def quem_sou(self):
        print ('Sou A')


class B(A):
    ...

    def quem_sou(self):
        print ('Sou B')

class C(A):
    ...

    def quem_sou(self):
        print ('Sou C')


class D(B, C):
    ...

    # def quem_sou(self):
    #     print ('Sou D')



d = D()
# d.quem_sou()

# print(D.__mro__)

#consigo ver a ordem de resolucao do mro, o caminho q o codigo faz para buscar os metodos
# procura primeiro em si mesmo e depois vai subindo
# o ideal é n ter muitas herancas multiplas
for d in D.mro():
    print(d)