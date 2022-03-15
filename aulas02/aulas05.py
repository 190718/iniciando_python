# Desenvolvendo um programa que calcule o comprimento de três retas.
# E informe se é possivel forma um triângulo.

r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3

if (soma1 > r3) & (soma2 > r2) & (soma3 > r1):
    print('É possivel formar um Triângulo!')
else:
    print('Desigualde triangular!')
    print('Não foi possivel formar um triângulo!')
