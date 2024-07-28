# GENERATION EXPRESSION, ITERABLES E ITERATORS EM PYTHON
# iteravel retem o valor
# iterator entrega um valor por vez ele sabe apenas qual o proximo valor,tem memoria curta
# generator são funções que sabem pausar
# todo generator tbm é um iterator, mas um iterator n é um generator
#Um generator não salva todos os valores na memoria, so o valor q estou usando

iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__()
iterator = iter(iterable) #é o mesmo codigo acima, mas utilizando a funcao do pyhton

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) #se eu chamar mais iteracoes do que tem na variavel da erro


generator = (n for n in range(1000))# para criar um generator basta colocar a
# funcao entre parenteses ()
lista = [n for n in range(1000)] 


# para ver o tamanho das coisas em python podemos utilizar o modulo sys
import sys
# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# O generator me entrega um valor por vez utilizando o next

print(next(generator))
print(next(generator))

for n in generator:
    if n%2 == 0:
        print(n)

#GENERATOR N TEM TAMANHO E NEM INDICE
