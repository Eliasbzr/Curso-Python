''' Laço de repeticao FOR '''
#utilizamos o for qdo sabemos qtas vezes iremos iterar (x q o laco roda)

'''
EXEMPLO DE WHILE COMUM
texto = 'Python'

i = 0
tamanho_string = len(texto)

while i <tamanho_string:
    print(texto[i])

    i +=1
'''


#Neste cod printamos cada letra dentro da palavra com sabemos q o numero 
#de repeticoes do laço é finito
palavra = 'Pyhton'
nova_palavra = ''
for letra in palavra:
    nova_palavra += f'*{letra}'
    print(letra)
print(nova_palavra)
