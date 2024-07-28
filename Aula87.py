# IS INSTANCE => Para saber o tipo do objeto


lista = ['a', 1,1.1, True, [0,1,2], (1,2),
         {0,1}, {'nome': 'Elias'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)

    elif isinstance(item, str):
        item.upper()

        print(item, isinstance(item, set))

    elif isinstance(item, (int, float)): #Entre parenteses ta procurando se o item é floau OU int
        print('num')
        print(item, item *2)
    else:
        print ('Outro')
        print(item)
        