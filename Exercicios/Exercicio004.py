#  FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO
# E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

tipo = input('Digite algo:  ')
print('você digitou "{}"'.format(tipo))
print(' "{}" é um dígito ? '.format(tipo), tipo.isdigit())
print( '"{}" é alfanumérico ? '.format(tipo),  tipo.isalnum())
print(' "{}"  tem valores decimais ? '.format(tipo), tipo.isdecimal())
print( ' "{}" é formato da tabela ASCII ? '.format(tipo),  tipo.isascii())
print(' "{}" são caracteres minúsculos ? '.format(tipo), tipo.islower())
print(' "{}" é composto por números ?'.format(tipo), tipo.isnumeric())
print(' "{}" contém espaços ?'.format(tipo), tipo.isspace())
print(' "{}" As primeiras letras estão em maíusculas ?'.format(tipo),tipo.istitle())
print(' "{}" são caracteres maiúsculos ?'.format(tipo), tipo.isupper())
