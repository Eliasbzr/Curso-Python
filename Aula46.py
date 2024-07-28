for i in range(10):
    if i==2:
        print('i é 2, pulando...')
        continue #volta ao inicio do laço

    if i ==8:
        print('i é 8, seu else nao executará')
        print('Saindo do laço')
        break #quebra a iteração, vai direto pro final

    for j in range(1,3):
        print(i,j)
else:
    print('for completo com sucesso')