#Mantendo estados dentro das classes

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print('Ja está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print('Não pode fotografar enquanto filma')
            return
        
        print(f'{self.nome} está fotografando...')

    def parar_filmar(self):
        if not self.filmando:
            print('pronta para uso')
            return
        print(f'{self.nome} parando filmagem')
        self.filmando =False



c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
