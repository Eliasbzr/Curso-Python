# @property + @setter - getter e setter no modo Pythônico
# - como getter
#  getter = obter o valor print(caneta.cor)
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected = _cor
        self._cor = cor #por convencao _cor o atributo nao deve ser utilizado tanto com 1 ou 2 _ (atributo protegido da classe)
        self._cor_tampa =None

    #metodos executam acoes
    @property
    def cor(self):
        return self._cor
       
    
    @cor.setter #utilizando o mesmo nome do metodo acima, mas transformando ele num setter
    # setter é interessante para colocar parametros dentro da variavel
    def cor(self, valor):
        print('dentro do setter', valor)
        #  atribuindo o valor a variaval
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa (self, valor):
        self._cor_tampa = valor



caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Preta'
print(caneta.cor_tampa)


