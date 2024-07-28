# import sys

# # import aula99_package
# # esta importando o package a pasta onde o modulo esta salco
# # mas sozinho o package n faz nada, ele n traz os modulos
# # dentro dele automaticamente

# from Aula99_package.modulo import soma_do_modulo
# print(soma_do_modulo(2,2))
# # desta forma posso chamar o modulo que esta dentro do package
# # eu chamo a pasta (package) . nome do arquivo modulo e import nome_do_modulo
# # dentro do arquivo de modulo

# # ou posso chamar desta forma:
# import Aula99_package.modulo
# print(Aula99_package.modulo.soma_do_modulo(2,2))
# # Assim fica muito mais coisas para escrever ao chamar o modulo
# # porem a identação fica mais facil de saber de onde estão vindo os
# # modulos


# # Ainda posso utilizar uma terceira forma

# from Aula99_package import modulo
# # dessa forma ao chamar o modulo o nome fica um pouco menor
# print(modulo.soma_do_modulo(2,2))

# from Aula99_package import modulo_b

# modulo_b.fala_oi()

from Aula99_package import soma_do_modulo, dobra
# dentro da pasta package criamos um arquivo com extamente o nome de __init__.py
# para enganar o python a trazer tudo que esta dentro desse package

print(soma_do_modulo(7,8))
dobra(125)