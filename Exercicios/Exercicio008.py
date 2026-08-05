# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS
# E MILÍMETROS

valor = float(input('Digite uma distância em metros: '))
kilometros = valor / 1000
hectometros = valor / 100
decametros = valor / 10
decimetros = valor * 10
centimetros = valor * 100
milimetros = valor * 1000

print('A medida de {:.2f} metros corresponde a:  '.format(valor))
print('{:.3f} kilometros \n{:.2f} hectometros\n{:.1f} decametros\n{:.0f} decimetros\n{:.0f} centímetros\n{:.0f} milímetros'.format(
    kilometros, hectometros, decametros, decimetros, centimetros,  milimetros))
