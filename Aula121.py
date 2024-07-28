# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

# Uma classe tem atributos e comportamentos:
# Classe carro tem os atributos:
#   marca => wolksvagen
#   modelo => Fusca
#   cor => Vermelho

# A classe tbm tem os comportamentos:
#   acelerar
#   frear
#   ligar


class Carro:
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} esta acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
# No metodo n preciso passar o nome dentro do parenteses, é como
# se estivesse utilizando uma função
fusca.acelerar()

# posso passar argumentos nomeados qto não nomeados em ordem

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()