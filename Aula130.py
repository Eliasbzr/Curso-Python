# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

# METODOS DE INSTANCIA SÃO OS SELF'S 
    def set_user(self,user):
        #setter
        self.user = user

    def set_password(self,password):
        #setter
        self.password = password
# ======================================
# MÉTODO DE CLASSE RECEBE A CLASSE EM SI
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

# ===================================
# METODO ESTATICO É UMA FUNCAO DENTRO DA CLASSE
    @staticmethod
    # n tem acesso ao self
    def soma (x,y):
        return(x+y)
    






# c1 = Connection()
# c1.set_user('Elias')
# c1.set_password('1234')

# print(c1.user, c1.password)

c1=Connection.create_with_auth('Elias','123')
print(c1.user)
print(c1.password)

print(c1.soma(34,87))