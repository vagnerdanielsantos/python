# FAÇA UM PROGRAMA QUE LEIA A LARGUAR E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA.
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS

altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))
area = altura * largura
print("Com uma altura de {:.2f} metros e uma largura de {:.2f} metros, temos uma área total de: {:.2f} metros quadrados.".format(altura, largura, area))
tinta = area / 2
print("Para pintar uma área de {:.2f} metros quadrados, serão necessários {:.2f} litros de tinta".format(area, tinta))
