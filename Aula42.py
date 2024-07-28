'''
'Quebrando strings em linhas
'''
'Para quebrar uma string em linhas'\
'basta usar a contra barra'\
'no final de cada linha'


frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)




texto = 'O Python é uma linguagem de programacao'\
        'multiparadigma '\
        'o Python foi criado por Guido van Rossun'


print(texto.count('Python')) 
''' contando qts vezes apareceu a palavra Python no texto'''
print(texto.count('a'))
'''contando qtd vezes apareceu a letra a no texto'''