"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40) ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

print ('Buscando Aluno: ')
print(salas[0][1])

print ('Buscando Aluno: ')
print(salas[2][2])

print ('Buscando 20: ')
print(salas[2][3][2])



salas = [['Amanda', 'Bruna', 'Carlos', 'Daniel'],
         ['Andre', 'Barbara', 'Carol'],
         ['Ana', 'Diego', 'Elias']]

for sala in salas:
    print (f'A Sala é: {sala}')
    for n, aluno in enumerate(sala):
        print (n, aluno)