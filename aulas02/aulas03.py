# Mostrando se o ano é Bissexto ou não.

# Importando biblioteca
from datetime import date

# Entrando com dados do tipo inteiro para o ano.
ano = int(input('Informa o Ano: '))

if ano == 0:
    ano = date.today().year
# Condição para informar se ano é bissexto ou não.
# Calculo para saber se o resto da divisão é igual a 0 (zero).
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é Bissexto'.format(ano))
# Condicional caso não for bissexto.
else:
    print('{} é um ano normal!'.format(ano))
