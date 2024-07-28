# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\elias\\Documents\\CURSOS\\Udemy\\Python do basico ao avancado\\Projeto\\' #usar 2 \ pro python entender melhor o caminho
caminho_arquivo += 'Aula116.txt'
# print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'w')#open é uma funcao do python ,em ordem primeiro o nome do arquivo e depois o modulo
#                                     # r (leitura), w (escrita), x (para criação) sempre abrimos e ja fechamos o arquivo
# # #
# arquivo.close()
# da forma escrita acima o arquivo precisa ser declarado abertura e fechamento
# utilizando a palavra with o n precisa fechar pq ja é automaticamente fechado


with open(caminho_arquivo, 'w+') as arquivo:
# o modo w apaga td q esta escrito no arquivo e reescreve
# o metodo write escreve no arquivo, para pular linhas utilizamos o n\
    arquivo.write('Linha 1 \n'
                  'Linha 2 \n'
                  '\n'
                  'linha 4 \n')
    arquivo.writelines('Linha 5 \n'
                       'Linha 6 \n')
    arquivo.seek(0,0) 
    #seek move o cursor dentro do arquivo
    # ao utilizar para leitura devemos posicionar o cursor
    # no topo da pagina para então utilizar o metodo read()

    for linha in arquivo.readlines():
        print(linha.strip())
    #metodo para ler as linhas de dentro do arquivo
    # print(arquivo.read())


# with open(caminho_arquivo, 'r') as arquivo:
# #com o 'r' podemos ler o arquivo no terminal
#     print (arquivo.read())

with open(caminho_arquivo, 'a+') as arquivo:
#com o 'a+' podemos escrever no arquivo apos a ultima linha e o '+' 
# utilizamos para ler, como se fosse um append
    arquivo.write('Linha 7 \n')
    arquivo.write('\n')
    arquivo.write('Linha 9')
    arquivo.seek(0,0)
    print (arquivo.read())

 
# import os

# # remove e unlik apagam o arquivo
# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)