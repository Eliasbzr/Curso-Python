# Exercício

#Aumente o preço dos produtos em 10%
#Gere novos_produtos por deep copy (copia profunda)


produtos = [
    {'nome': 'Produto 5', 'preco':10.00},
    {'nome': 'Produto 1', 'preco':22.32},
    {'nome': 'Produto 3', 'preco':10.11},
    {'nome': 'Produto 2', 'preco':105.87},
    {'nome': 'Produto 4', 'preco':69.90},
]

# Ordene os produtos por nome decrescente
# gere produtos_ordenados_por_nome por deep copy

# Ordene os produtos por preco decrescente
# gere produtos_ordenados_por_preco por deep copy
print("Produtos")
print(*produtos, sep='\n')

print("")
print("")




# Ex 1 
import copy

novos_produtos = [ 
   {**p,'preco': p['preco']*1.1,}
    for p in copy.deepcopy(produtos)

]
print("Novos produtos")
print(*novos_produtos, sep='\n')
 

#Ex 2 = Ordenando por nome produto
print(""),
print('')


produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), 
                                     key=lambda n:n['nome'], reverse=True)

print("Produtos ordenados por nome")
print(*produtos_ordenados_por_nome, sep='\n') 


print(""),
print('')

# 3
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), 
                                      key=lambda p: p['preco'],reverse=False)

print("Produtos ordenados por preço")
for produto in produtos_ordenados_por_preco:
    print(produto)