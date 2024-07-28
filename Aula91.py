#Introducao a generator funcitions em python
# toda funcao generator em python utiliza a para yield no lugar de return
# as funcoes c generator pausam a cada yield, ele encontra o primeiro executa e procura
# o proximo

# generator = (n for n in range (1000000))

def generator (n=0):
    yield 1 #pausa a funcao
    print("Aqui poderia ser um codigo")
    yield 2 #nova pausa
    print("Aqui poderia ser outro codigo")
    yield 3 
    print('E aqui tbem')
    return 'Acabou' #aqui encerra o loop de codigo
    # print('n tem mais nada // inalcançavel')


gen = generator(n=0)

for n in gen:
    print(n) #executando de forma dinamica


# criando uma mais uma funcao com yield

def generator(n=0, maximun=10):
    while True:
        yield n #aqui pausa
        n +=1

        if n>maximun: #se o n for maior que 10 ele finaliza
            return

gen = generator()
for n in gen:
    if n%2 !=0:
        print(n)