#Método especial __call__
#callable é algo que pode ser executado com parenteses
#em classes normais, __call__ faz a instancia de uma
# classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self,nome):       
        print(nome,'está chamando', self.phone)

call1 = CallMe('1234678')
call1('Elias')