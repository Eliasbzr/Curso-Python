# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

class MinhaString (str):
    def upper(self):
        print('Chamou o UPPER')
        retorno = super().upper() #estou chamando o upper da superclasse, o upper q esta no def
        print('Pos Upper')
        return retorno
        #depois do return n executa mais nada dentro do def

string = MinhaString("eLias")

# print(string.upper())

class A:
    atributo_a ='valor de a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('Metodo de A')


class B(A):
    atributo_b = 'Valor de b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo (self):
        print('Metodo de B')

class C(B):
    atributo_c = 'Valor de c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo() #implicitamente (automaticamente) p python coloca dentro dos parenteses (C, Self)
                         # portanto a superclasse de C é B

        super(B, self) #Aqui eu estou falando de onde ele parte para procurar a superclasse
                       #esta partindo de B, logo a superclasse é A
        A.metodo(self)
        B.metodo(self)
        print('Metodo de C')

#  De acordo com o esquema acima em C temos tds os atributos pq o atributo B veio de herança para B
#  e C herdou os atributos de B q era A e B
#  o metodo se manteve apenas 1 o metodo de C pois tds tem o mesmo nome e sempre é procurado na 1º instancia
#  da classe para cima

# help(C)
# com o help podemos ver o caminho q o metodo faz, do metodo C para cima até object pq tudo no python é um object
# class C(B)
#  |  Method resolution order:
#  |      C
#  |      B
#  |      A
#  |      builtins.object


# ex = C()

# print (ex.atributo_a)
# print (ex.atributo_b)
# print (ex.atributo_c)

# ex.metodo()

# print(C.mro())
# print(B.mro())
# print(A.mro())
ex = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
ex.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()