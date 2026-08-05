# DESENVOLVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO.
# CALCULE E MOSTRE A SUA MÉDIA

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02) / 2

print('A média ente o número {:.1f} e {:.1f} é: {:.1f} '.format(nota01, nota02, media))
