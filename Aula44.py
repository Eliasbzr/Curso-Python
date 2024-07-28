'''
FOR + Range

rang -> (start, stop, step)

'''

numeros = range(10) #passando apenas um parametro ele se torna o stop, até onde a iteracao vai parar
for numero in numeros:
    print (numero)
    
pares = range(0,20,2)
print ('Pares:')
for par in pares:
    print(par)

impares = range (1,20,2)
print ('Impares:')
for impar in impares:
    print(impar)