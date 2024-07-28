# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
#Sobrecarga de metodos (overload)
#Sobreposição de metodos(override)

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self)-> bool: #depois da setinha n faz nada em python isso é para os dev's se comunicarem é uma dica para seu cod 'type anotation'
        ...

class NotificacaoEmail(Notificacao): #(Notificação) está deixando de heranca seus parametros para as classes filhas
    def enviar(self)-> bool:
        print ('E-mail enviando:', self.mensagem)
        return True
        
class NotificacaoSMS(Notificacao):
    def enviar(self)-> bool:
        print ('SMS enviando:', self.mensagem)
        return True


# n = NotificacaoEmail('teste de mensagem')
# n.enviar()

def notificar(notificacao: Notificacao): #estou falando pro python utilizar td o q vem de Notificacao
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificação nao enviada')

# A notificação se comporta de forma polimorfica, ou seja a 'notificação' se comporta de formas diferentes em cada uso

notificar(NotificacaoEmail('Notificando via e-mail'))

notificacao_sms = 'Enviando notificação via sms'

notificar(NotificacaoSMS(notificacao_sms))