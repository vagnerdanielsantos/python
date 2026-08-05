# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM GRAUS CELSIOS PARA
# TEMPERATURA EM GRAUS FAHRENHEIT.

celsius = float(input("Digite a temperatura em graus celsius: "))
temperatura = (celsius * 1.8) + 32
print("A temperatura de {:.1f} graus celsius convertida em temperatura fahrenheit equivale a {:.1f}. ".format(celsius, temperatura))
