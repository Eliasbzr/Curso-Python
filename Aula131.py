# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor


    @property
    # como se fosse para arrumar o codigo
    # a variavel antes se chamava cor tinta agr se chama so cor
    def cor(self):
        print('Tbm posso executar acoes')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        
        return(f'cor da tampa: {self.cor}')

caneta = Caneta('Vermelha')
print(caneta.cor)
print(caneta.cor_tampa)
print(caneta.cor)
print(caneta.cor)







# METODO TRADICIONAL DE GETTER
# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('pegando a cor')
#         return self.cor_tinta
    

# caneta = Caneta('Azul')

# print(caneta.cor_tinta)
# print(caneta.get_cor())