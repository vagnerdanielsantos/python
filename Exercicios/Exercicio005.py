# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

valor = int(input('Digite um número inteiro:  '))
sucessor = valor + 1
antecessor = valor - 1

print('Analisando o valor {}, seu sucessor é {} e o seu antecessor é {}.'.format(valor, sucessor, antecessor))
