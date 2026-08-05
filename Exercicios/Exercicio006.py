# FAÇA UM ALGORÍTMO QUE LEIA UM NÚMERO E MOSTRE NA TELA O SEU  DOBRO, TRIPLO E RAIZ QUADRADA

valor = int(input('Digite um número inteiro: '))
dobro = valor * 2
triplo = valor * 3
raiz_quadrada = valor ** (1/2)

print('Analisando o valor {}, o dobro deste valor é : {}'.format(valor, dobro))
print('Analisando o valor {}, o triplo deste valor é:  {} '.format(valor, triplo))
print('Analisando o valor {}, a sua raiz quadrada é: {:.2f}'.format(valor, raiz_quadrada))
