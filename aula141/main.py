# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.LogError('Falha no acesso')
# lp.LogSucess('Sucesso no acesso')

# lf = LogFileMixin()
# lf.LogError('Falha no acesso')
# lf.LogSucess('Sucesso no acesso')


from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')

iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()