a = input('Digite algo: ')
a2 = input('Mais alguma coisa: ')
print(a, a2)
# Informando se o dado escrito é Alfabético.
print('É Alpha? {}, {}'.format(a.isalpha(), a2.isalpha()))
#-----------------------------------------------------------#
print('É Numerico? {}'.format(a.isnumeric()))
print('É AlphaNumerico? {}'.format(a.isalnum()))
print('Contem espaços? {}'.format(a.isspace()))
print('Contem capitalizada? {}'.format(a.istitle()))
# uma palavra capitalizada é uma palavra que inicia com maiuscula
# Ex: Python, Brasil, Jenne, Pandora, etc.
#--------------------------------#
# isalpha, isnumeric, isalnum, etc. São metodos do tipo bool
