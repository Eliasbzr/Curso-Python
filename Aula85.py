
#USANDO FOR DENTRO DO OUTRO

# do modo tradicional fazemos assim:

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))



# Ja em list comprheension:
lista = [
    (x, y) # aqui eu incluo as variaveis da lista
    for x in range (3) #for externo
        for y in range (4) #for interno
    ]




print(lista)