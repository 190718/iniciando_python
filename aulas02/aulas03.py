# Mostrando se o ano é Bissexto ou não.

# Entrando com dados do tipo inteiro para o ano.
ano = int(input('Informa o Ano: '))
# Calculo para saber se o resto da divisão é igual a 0 (zero).
bissexto = ano % 4
# Condição para informar se ano é bissexto ou não.
if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
# Condicional caso não for bissexto.
else:
    print('Ano normal!')
