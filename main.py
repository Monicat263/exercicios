#  1 - Reconhecendo tipos de dados via Python:
#  Objetivo
# Neste problema, revisaremos os tipos de dados vistos em aula e praticaremos
# como os reconhecer a partir de expressões dadas.
# Especificação
# Diga qual é o tipo de cada uma das expressões abaixo:

# * 5
# * 5.0
# * 5 > 1
# * '5'
# * 5 * 2
# * '5' * 2
# * '5' + '2'
# * 5 / 2
# * 5 // 2
# * [5, 2, 1]
# * 5 in [1, 4, 6]
print('Exercicio 01 - Resolução: ')
a = 5
b = 5.0
c = 5 > 1
d = '5'
e = 5 * 2
f = '5' + '2'
g = 5 / 2
h = [5, 2, 1]
i = 5 in [1, 4, 6]

print('{} é do tipo {}'.format(a, type(a)))
print('{} é do tipo {}'.format(b, type(b)))
print('{} é do tipo {}'.format(c, type(c)))
print('{} é do tipo {}'.format(d, type(d)))
print('{} é do tipo {}'.format(e, type(f)))
print('{} é do tipo {}'.format(g, type(g)))
print('{} é do tipo {}'.format(h, type(h)))
print('{} é do tipo {}'.format(i, type(i)))
print('*'* 30)

print('# Também posso resolver com a função format ')
print('# e utilizar  a tupla')

results = [
    (5, type(5)),
    (5.0, type(5.0)),
    (True, type(True)),
    ('5', type('5')),
    ('10', type('10')),
    (2.5, type(2.5)),
    ([5, 2, 1], type([5, 2, 1])),
    (False, type(False))
]

for lista in results:
    print("{:<20} {:^10}".format(str(lista[0]) + " é do tipo", str(lista[1])))





