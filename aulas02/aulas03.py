# Mostrando se o ano é Bissexto ou não.

# Entrando com dados do tipo inteiro para o ano.
ano = int(input('Informa o Ano: '))
# Calculo para saber se o resto da divisão é igual a 0 (zero).
bissexto = ano % 4
# Condição para informar se ano é bissexto ou não.
if bissexto == 0:
# Segundo calculo para  confirmar se ano é bissexto.
    mais1 = ano % 100
    print('Bissexto')
# Condicional caso não for bissexto.
else:
    print('Ano normal!')
