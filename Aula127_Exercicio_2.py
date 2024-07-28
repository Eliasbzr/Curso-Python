import json 
from Aula127_Exercícios import Pessoa



with open('aula127.json', 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)

    
p1 = Pessoa(**pessoas[0])
p2 = Pessoa(**pessoas[1])
p3 = Pessoa(**pessoas[2])


for p in pessoas:
    p = Pessoa(**p)
    print(p.__dict__)


print(p1.__dict__)
print(vars(p2))
print(vars(p3))


