# Valores Truthy e Falsy, tipos mutaveis e imutaveis
# Mutaveis = [], {}, set()
# Imutáveis = (), "str", 0, 1.0,Nome,False, range(1,10)

# Os itens abaixo são todos Falsy 
lista = [] #lista vazia é falsy 
dicionario = {} #dicionario vazio é falsy
conjunto=set() #set vazio é falsy
tupla = () #tupla vazia é falsy
string = '' #é falsy
inteiro = 0 #0 é falsy
flutuante = 0.0 # é falsy
nada = None #é falsy
falso = False #é falsy
intervalo = range(0) #range vazio é falsy

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print('TESTE'), falsy('TESTE')
print(f'lista', falsy(lista))