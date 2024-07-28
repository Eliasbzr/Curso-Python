#Empacotamento e desempacotameno de dicionários

a, b = 1,2
a,b= b,a
print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a,b = pessoa
# print(a,b) #dessa forma desempacoto a chave

# a,b = pessoa.values()
# print (a,b) #assim desempacoto os valores

# a,b = pessoa.items()
# print (a,b) #retorna uma tupla com a chave e valor

# (a1,a2),b = pessoa.items()
# print (a1,a2,b) #tbm é possível desempacotar internamente

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.6,
}

print(pessoa, dados_pessoa)

#Unindo os dicionários

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

#Ainda posso incluir mais chaves na uniao do novo dicionário
pessoa_completa = {**pessoa, **dados_pessoa, 'sexo': 'F', 'turma': '2ºB'}
print(pessoa_completa)

#KWARGS = Keyword arguments = argumentos nomeados
#kwargs são referenciados sempre com 2 '*'
def argumentos (*args, **kwargs):
    for chave, valor in kwargs.items():
        print (f'{chave} | {valor}')

argumentos(nome='Joana', numero=45)

#desempacotar um dicionário

argumentos(**pessoa_completa)