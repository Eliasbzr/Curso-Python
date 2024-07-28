# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self): #a classe __repr__ é para os devs comunicarem como é a representacao do valor
        #class_name = self.__class__.__name__ #AS DUAS INSTANCIAS DE class_name sao a mesma coisa
        class_name = type(self).__name__
        return f'{class_name} | (x={self.x}, y={self.y})'

    # def __str__(self): # o modulo usa principalemente o str, e o str apenas mostra a string
    #     return f'{self.x},{self.y}'

    def __add__(self, other):
        novo_x= self.x + other.x
        novo_y= self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self,other)->bool:
        resultado_self= self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

p1 = Ponto(1,2)
p2 = Ponto(34,78)
p3 = p1 + p2
p4 = p1 > p2

print(p1)
print(repr(p2)) #assim eu vejo o repr de um modulo que tenha str dentro, pois o str é preferencial no print
print(f'{p2!r}') #dessa forma  eu tbm chamo o repr do modulo, se trocar para s chamaria a string

print(f'{p3!r}')
print(p4)