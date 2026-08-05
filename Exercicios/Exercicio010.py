# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UM PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS
# DOLARES E EUROS ELA PODE COMPRAR.
# CONSIDERE  US$ 1.00 = R$ 3.27
# CONSIDERE € 1.00 = R$ 5.86

dinheiro = float(input("Informe qual o valor deseja converter: "))
euro = dinheiro * 5.86
dolar = dinheiro * 3.27

print("O valor de R$ {:.2f} reais convertido em dólar é de US$ {:.2f} dólares". format(dinheiro, dolar))
print("O valor de R$ {:.2f} reais convertido em euros é de \u20AC {:.2f} euros".format(dinheiro, euro))
