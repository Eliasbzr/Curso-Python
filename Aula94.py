# TRY EXCEPT ELSE E FINALY

#o FINALY SERVE PRA EXECUTAR UM CODIGO INTEIRO 
# MESMO COM ERRO E EXECUTAR O 'ULTIMO PASSO'


try:
    print( 'Try executado')
    8/0
except ZeroDivisionError:
#tbm posso colocar varios excepts dentro
    print('Erro de 0')
else:
    print('Sem erros')
finally:
#o finaly sempre é executado independente do q houver
# mesmo o erro sendo acusado o finaly executa
    print( 'Finaly executado')




