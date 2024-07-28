print (
    '██╗███╗░░░███╗░█████╗░',
    '██║████╗░████║██╔══██╗',
    '██║██╔████╔██║██║░░╚═╝',
    '██║██║╚██╔╝██║██║░░██╗',
    '██║██║░╚═╝░██║╚█████╔╝',
    '╚═╝╚═╝░░░░░╚═╝░╚════╝░',sep='\n')

nome = input('Digite o nome: ')
altura = float(input('Digite a altura em mts separados por .: '))
peso = float(input('Digite o Peso: '))
imc = round(peso / (altura **2),1)
p_imc = 'a'
if imc <18.5:
    p_imc = 'Magreza'
elif imc >18.5 and imc<=24.9:
    p_imc = 'Normal'
elif imc >24.9 and imc <=29.9:
    p_imc = 'Sobrepeso'
elif imc >29.9 and imc <=39.9:
    p_imc = 'Obesidade'
else:
   p_imc = 'Obesidade Grave'


print (f'Nome: {nome.ljust(10)} | Altura: {str(altura).ljust(10)} | Peso: {str(peso).ljust(10)} | IMC: {imc} classificado como: {p_imc}')