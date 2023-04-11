import numpy as np
# Imagine que foram atribuídos valores para variáveis chamadas x, y e z.
# Para cada um dos itens abaixo, escreva uma expressão python que calcule os
# valores desejados em função de x, y e z.

# a) A soma de x, y e z.
#
# b) A média dos valores de x, y e z.
#
# c) Ache o maior valor dentre x, y e z.
#
# d) Ache a mediana entre x, y e z. Lembre-se de que a mediana é o
# "valor do meio". Você pode calcular isso usando as expressões dos outros
# itens. # Para tanto, monte uma expressão que é a expressão do item a
# subtraído do maior e do menor valor.


x = 2
y = 5
z = 3


soma = (x + y + z)
media = (x + y + z)/3


print('a) soma:', + soma)

print('*' * 50)

print('b) média:')
print('{:.2f}'.format(media))

print('*' * 50)

print('c) Ache o maior valor dentre x, y e z.')
print('Primeira Solução:')

if x > y and x > z:
    print(x, 'é o maior valor')
elif y > x and y > z:
    print(y, 'é o maior valor')
else:
    print(z, 'é o menor valor')

print('*' * 50)
print('Segunda Solução, usando input do usuário:')

f = float(input("Digite o valor de f: "))
g = float(input("Digite o valor de g: "))
h = float(input("Digite o valor de h: "))

if f > g and f > h:
    print(f, 'é o maior valor')
elif g > f and g > h:
    print(g, 'é o maior valor')
else:
    print(h, 'é o maior valor')

print('*' * 50)

print('Terceira Solução, usando função maior:')

maior_valor = max (f , g , h)
print(maior_valor,'é o maior valor')

print('*' * 50)
print('d), Cálculo da mediana:')
print(' Primeira solução , utilizando a biblioteca numpy e sorted :')
print('Numpy para médiana e sorted para ordenar a lista :')

lista = [x,y,z]
lista_valores = sorted(lista)
mediana = np.median(lista_valores)
print('A mediana do conjunto de dados:',lista_valores, 'é: ',  mediana)


print('*' * 50)
print('d), Cálculo da mediana:')
print('Segunda solução ,sem utilizar a biblioteca Numpy :')
print('Instruções: Ordenar a lista, verificar se a lista possui elementos ')
print('pares e impares sendo:')
print('Se houver um número impar a mediana é o número do meio.')
print('Se houver um número par a mediana é a soma dos dois valores centrais.')

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n_elementos = len(lista_ordenada)
    if n_elementos % 2 == 0:
        # Se for par, calcula a média dos dois elementos centrais
        i_central = n_elementos // 2
        i_central2 = i_central - 1
        mediana = (lista_ordenada[i_central] + lista_ordenada[i_central2])/2
    else:
       # Se for impar, retorna o elemento central
        i_central = (n_elementos -1) // 2
        mediana = lista_ordenada[i_central]

    return lista_ordenada,mediana
# Aqui eu chamo a função, de uma lista qualquer,ordeno,depois faço a impressão
# para ter certeza que a função está funcionando.

teste_lista = [1000,124,380]
teste_lista.sort()
lista_ordenada,mediana = calcular_mediana(teste_lista)
print("Lista ordenada:", lista_ordenada)
print("A mediana da lista é:", mediana)


print('*' * 50)
print('Expressões')

# a) criem uma nova lista e atribuam a uma variável chamada romanos, contendo as
# strings 'Julius', 'Augustus', 'Brutus' e 'Cassius'.
#
# b) criem uma lista e atribuam a uma variável chamda ingleses, contendo as
# strings 'Dickens', 'Austen', 'Henry' e 'Elizabeth'.
#
# c) criem uma lista e atribuam a uma variável chamada governantes, que contém
# os dois primeiros elementos da lista romanos e
# os dois últimos elementos da lista ingleses. Use expressões de manipulação de
# lista; não copie os dados apenas manualmente.
# Orientações Adicionais

print('*' * 50)
print('Resolução a)')

romanos = ['Julius', 'Augustus', 'Brutus','Cassius']
print(romanos)

print('*' * 50)
print('Resolução b')

ingleses = ['Dickens','Austen','Henry','Elizabeth']
print(ingleses)

print('*' * 50)
print('Resolução c')
# ressalto a regra de exclusivo, nesse caso para aparecer os dois primeiros
# preciso ir até o terceiro para selecionar os dois primeiros
nova_list = romanos[0:2] + ingleses[2:4]
print(nova_list)


