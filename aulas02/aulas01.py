# Importando biblioteca de calculos matematicos.
import math
# "from math import sqrt" nesse formato importa somente operação de raiz (sqrt).
# Usando "from ... import ...." expecifica o item da biblioteca, e não ela toda.

# Entrando com valores inteiros para calcular raiz.
num = int(input('Informe a raiz de: '))
# Calculando raiz usandoa biblioteca Math.
raiz = math.sqrt(num)
# Imprimindo valores e resultado da raiz.
# O valor da raiz vai sair "quebrado".
print('A raiz de {} é igual a {}'.format(num, raiz))
# Formato de arredondamento do resultado.
print('Arredondamento: {}'.format(math.floor(raiz)))
# Reduzindo a 2 casas depois da virgula.
print('valor reduzido: {:.2f}'.format(raiz))
# ":.2f" não faz parte da biblioteca, é objeto de formatação padrão da linguagem.
# ".2" casas decimais, "f" flutuantes (float).