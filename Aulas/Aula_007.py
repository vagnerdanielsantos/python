numero01 = int(input('Digite um número: '))
numero02 = int(input('Digite outro número: '))

soma = numero01 + numero02
subtracao = numero01 - numero02
multiplicacao = numero01 * numero02
divisao = numero01 / numero02
potenciacao = numero01 ** numero02
divisao_inteira = numero01 // numero02
divisao_resto = numero01 % numero02

print('A soma entre {} e {} é: {}'.format(numero01, numero02, soma))
print('A subtração entre {} e {} é {}'.format(numero01, numero02, subtracao))
print('A multiplicação entre {} e {} é {}'.format(numero01, numero02, multiplicacao))
print('A divisão entre {} e {} é {:.2f}'.format(numero01, numero02, divisao))
print('A potenciação entre {} e {} é {}'.format(numero01, numero02, potenciacao))
print('A divisão inteira entre {} e {} é {}'.format(numero01, numero02, divisao_inteira))
print('O resto da divisão entre {} e {} é {}'.format(numero01, numero02, divisao_resto))
