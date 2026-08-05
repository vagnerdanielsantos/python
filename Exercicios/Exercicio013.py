# FAÇA UM ALGORÍTIMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO COM
# 15% DE AUMENTO.

salario = float(input("Informe seu salário atual: R$ "))
novoSalario = salario +(salario * 0.15)
print("Com um acrescimo de 15%, o salário anterior de R$ {:.2f}, agora é de R$ {:.2f}".format(salario, novoSalario))
