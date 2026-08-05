# FAÇA UM ALGORÍTIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM
# 5% DE DESCONTO

preco = float(input("Informe o preço do produto: R$ "))
novoPreco = preco - (preco * 0.05)
print("O valor de R$ {:.2f} com um desconto de 5% é de R$ {:.2f}".format(preco, novoPreco))
