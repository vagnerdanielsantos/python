##  ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
# ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO.
##  CALCULE O PREÇO A PAGAR SABENDO QUE O CARRO CUSTA R$ 60.00 POR DIA E R$ 0.15 POR KM RODADO.

percorrido = float(input("Digite quantos quilometros foram percorridos: "))
dias = int(input("Digite quantos dias o veículo foi alugado: "))
preco = (percorrido * 0.15) + (dias * 60)
print("O valor a pagar após ter utilizado o veículo por {} dias e por {:.1f} quilometros é de: R$ {:.2f}. ".format(dias, percorrido, preco))
