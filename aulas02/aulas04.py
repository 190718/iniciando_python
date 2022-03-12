# Calculando o almento de salario.
# 10% para maior que 1250.00.
# 15% para menor ou igual a 1250.00.

salario = float(input('Informe seu salário atual: R$'))
novoSalario = salario * 0.10

if salario > 1250.00:
    ajuste = salario * 0.10
    novoSalario = salario + ajuste
    print('Ajuste de 10%: R${:.2f}'.format(ajuste))
    print('Salário ajustado: R${:.2f}'.format(novoSalario))
else:
    ajuste = salario * 0.15
    novoSalario = salario + ajuste
    print('Ajuste de 15%: R${:.2f}'.format(ajuste))
    print('Salário ajustado: R${:.2f}'.format(novoSalario))
