# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

class Pessoa:
    def __init__(self, nome, idade, peso, altura ):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

import json


p1 = Pessoa(nome='Elias', idade=32, peso=78, altura=176)
p2 = Pessoa(nome='Joao', idade=34, peso=98, altura=186)
p3 = Pessoa(nome='Maria', altura=156, idade=38, peso=56)

# caminho_arquivo = 'C:\\Users\\elias\\Documents\\CURSOS\\Udemy\\Python do basico ao avancado\\Projeto\\' #usar 2 \ pro python entender melhor o caminho
# caminho_arquivo += 'Aula127.json'

bd = [p1.__dict__,
      vars(p2),
      p3.__dict__
      ]

with open('aula127.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        bd,
        arquivo,
        ensure_ascii=False, #formata com a codificação de caracteres do seu sistema
        indent=2, #Aqui ja formata o texto
        
    )



