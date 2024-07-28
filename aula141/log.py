# ABSTRACAO
#abstracao é um dos pilares da programacao orientada ao objeto

import os
from pathlib import Path

LOG_FILE = Path(__file__).parent/'log.txt' #ate o parent ele pega o caminho deste arquivo

class limpa:
    os.system('cls')


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemento o médoto log')
    
# método abstrato:   
    def LogError(self, msg):
        return self._log(f'Error: {msg}')
    

    def LogSucess(self, msg):
        return self._log(f'Sucess: {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print("Salvando no log: ", msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
         
      

class LogPrintMixin(Log):
    def _log(self, msg):
         print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    limpa()
    lp = LogPrintMixin()
    lp.LogError('Falha no acesso')
    lp.LogSucess('Sucesso no acesso')

    lf = LogFileMixin()
    lf.LogError('Falha no acesso')
    lf.LogSucess('Sucesso no acesso')


