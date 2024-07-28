#Context Manager com função - Criando e usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo): #isso é um generator
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo #esse yiel funciona como uma 'pausa' que le o with abaixo -- yiel tbm transforma a funcao em generator
    except Exception as e:
        print ('Ocorreu um erro',e)
    finally:
        print('Fechando arquivo')
        arquivo.close

with my_open ('Aula150.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write("Linha2 \n",4567)
    arquivo.write('Linha3 \n')
    print('WITH', arquivo)