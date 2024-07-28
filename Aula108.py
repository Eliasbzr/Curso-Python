#Count é um iterador sem fim
#count é filho do itertools

from itertools import count

c1 = count(10, 15) # 10 => aqui eu posso passar apenas o inicio
                              # 15 => step, de qts em qts pula
c1 = count(step=10, start=15)       #ainda posso nomear os argumentos, caso n nomeie a ordem é
                                    # 1º o inicio depois o step

c2 = count(step=50) # tbm posso informar apenas o step


# for i in c1:
#     print(c1) #conta pra sempre

print('c1', hasattr(c1, '__iter__')) #perguntando se o count tem um iterator
print('c1', hasattr(c1, '__next__')) #tbm tem o next, pois é um iteravel

for i in c1:
    if i >100: 
        break #o break para o codigo p n gerar um loop infinito
    
    print(i)


for i in c2:
    if i >=500:
        break

    print(f'Passo {i}')