# Desenvolvendo um programa que pergunte a distância de uma viagem em Km.
# Calcula o preço da passagem.
# Cobrando R$0.50 por Km, para viagem de até 200Km.
# E para viagem mais longa, R$0.45 por Km.


print('Boletim de viagem!')
# Informando a distancia que vai percorre em Km.
distanciaInicial = float(input('Informe a distancia Km: '))
# Iniciando a condição para distancia menor ou igual a 200Km.
if distanciaInicial <= 200:
    # calculando o valor para a distância percorrida.
    valor01 = distanciaInicial * 0.50
# Mostrando ovalor da viagem.
    print('Valor da viagem: R${:.2f}'.format(valor01))
# Iniciando condicional para segunda opção.
else:
    # Calculando valor para distância percorrida.
    valor02 = distanciaInicial * 0.45
# Mostrando valor de viagem maior que 200Km.
    print('Valor da viagem: R${:.2f}'.format(valor02))
