
name = str(input('Nome: '))
materia = input('Matéria: ')
notaAlu = int(input('Nota da matéria: '))
notaOk = 7

# tomada de decisão
# Se notaAlu é menor ou igual a notaOk
if notaAlu <= notaOk:
    print('Recuperação!')
# Se não, mostre...
else:
    print('Passou Ok!')

# Mostrando nome e matéria.
print('{}, {}!'.format(name, materia))
