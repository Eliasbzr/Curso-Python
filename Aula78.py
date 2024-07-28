# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
#set(iterável) ou {1, 2, 3}

s1 = set()#criando um set vazio 
print(s1)
print(type(s1))

# colocando um iteravel dentro do set
s1 = set('Elias')
print(s1)

#set com dados
s2 = {'Elias', 1,2,3}
print (s2)
# como um dicionário, mas sem par de chave e valor


#Sets são eficientes para remover valores duplicados de iteráveis.
#O SET N GARANTE A ORDEM DOS VALORES
#- Não aceitam valores mutáveis;
s1_im = {1,2,3,'arroz', [44,55,66]} #int & str= imutavel| lista = mutavel n pode virar um set
print(s1_im) #TypeError: unhashable type: 'list'

#- Seus valores serão sempre únicos;
s1 = {'a','s','a','a'}
print(s1)
sn = {1,1,1,2,2,2,3,33,3,3,4,5}
print(sn)
    #o set elimina automaticamente os valores duplicados
    # tbm podemos transformar listas, tuplas e etc em set para limpar duplicidades
s1_lista = [1,1,1,'a','a','a'] #lista duplicada
s1_set= set(s1_lista) #set tirando a duplicidade
s1_set = list(s1_set) #lista sem duplicados
print(s1_set)

# - não tem índexes;
#s1 = {1,2,3}
#print(s1[0]) #TypeError: 'set' object is not subscriptable
             # n da pra acessar por indice



# - são iteráveis (for, in, not in)
s1 = {1,2,3}
print(3 in s1) #resulta em booleano
print(3 not in s1)

for numero in s1:
    print(f'numero: {numero}')


#Métodos úteis:
#sadd, update, clear, discard
s1 = set()
s1.add('Elias')
s1.add(1)
#s1.update('Hello word') #o updade se comporta como o add, mas dessa forma entra letra por letra
s1.update(('Hello word', 1,2,3)) #dessa forma entra a palavra inteira, um iteravel dentro do outro
#s1.clear() #aqui limpa tudo
s1.discard(1) #posso passar o valor que eu quero descartar do set
print(s1)


# Operadores úteis:
s1 = {1,2,3}
s2 = {2,3,4}

# união | união (union) - Une
s3 = set.union(s1,s2) # ou 
s3 = s1 | s2
print(f'Uniao: {s3}')

# intersecção & (intersection) - Itens presentes em ambos
s4 = s1 & s2 #ou
s4 = set.intersection(s1,s2)
print(F'Intersecção: {s4} ')

# diferença - Itens presentes apenas no set da esquerda
s5 = s1 - s2 #ou
s5 = set.difference(s1,s2)
print(f'Diferenca: {s5}')

# diferença simétrica ^ - Itens que não estão em ambos nao importa a ordem 
s6 = s1 ^ s2
s6 = set.symmetric_difference(s1,s2)
print(f'Diferenca simetrica: {s6}')


# teoria dos conjuntos da mátemática
