# Recarregando Modulos
# tds os modulos no python sao singleton, ou seja são carregados apenas 1 vez
# sem a necessidade de recarrega-los novamente pois ja estao salvos na memoria por
# questao de eficiencia

# Caso eu queira regarregar um modulo posso utilizar a biblioteca importlib

import importlib #c essa biblioteca eu posso recarregar o modulo

import Aula98_m

print(Aula98_m.variavel)

for i in range (10):
    print(i)
    importlib.reload(Aula98_m) # aqui estou regarregando o modulo que seja executado
                               #novamente, utilizando o atributo reload não mais 
                               #o import



print('fim')

#NÃO É MUITO FREQUENTE A RECARGA DO MODULO, MAS PODE HAVER A NECESSIDADE
# EM ALGUM MOMENTO
