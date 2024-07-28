#Dictionary Comprehension e Set Comprehension

produto = {
            'nome':'Caneta Azul',
            'preco': 2.5,
            'categoria':'Escritório',

}

dc = {
    chave.upper(): valor.upper() #tentando trazer tds os valores em maiusculo
    if isinstance(valor, str) else valor #mas como temos um int precisamos colocar um if para aplicar apenas a str
    for chave, valor in produto.items()
    # if chave == 'categoria' #trazendo apenas se o if for atendido
    if chave !='categoria' #!= é a representacao de diferente de, tbm so traz se a chave for atendida
}

#Trazendo informações de uma lista que for parecido com dicionario
lista = [
    ('a', 'Valor a'),
    ('b', 'Valor b'),
    ('x', 'Valor x')

]

dc = {

    chave: vlr 
    for chave, vlr in lista


}



# print (dc)

#SET COMPREHENSION

# s1 = {i**2 for i in range (10) if i**2 %2 ==0} #tbm é possivel utilizar o if
s1 = {i**2 for i in range (10) if i**2 %2 !=0} #tbm é possivel utilizar o if
print (s1)