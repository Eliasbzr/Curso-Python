# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar O INIT SERÁ UTILIZADO EM 99,99% DOS CASOS PARA CRIACAO DE OBJ
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:
    def __new__(cls, *args, **kwargs):  #NEW DEVE RETORNAR UM OBJETO  // arg para n me importar com quantos argumentos viram no init
        print ('isto é antes de criar a instancia')
        instancia = super().__new__(cls)
        print ('Depois da instancia criada')
        return instancia

    def __init__(self, x):
        self.x = x
        print (self.x)

    def __repr__(self):
        return f'A({self.x})'
    

a = A(154)