"""Suponha que você já tenha uma lista definida, chamada dados, contendo três
strings: o primeiro nome, o nome do meio e o sobrenome
de uma pessoa, nessa ordem. Escreva uma expressão que produza uma string que
consiste no sobrenome da pessoa
seguido de uma vírgula e espaço, depois o primeiro nome e um espaço,
depois a inicial do meio da pessoa seguida de um ponto.
Assim, por exemplo, se a lista dados for igual a
['Pedro', 'Álvares', 'Cabral'],sua expressão produzirá
a string 'Cabral, Pedro Á."""

print('*' * 50)
print('Resolução lista 2,questão a)')

dados = ['Pedro', 'Alvares', 'Cabral']
#print(dados)

nome_meio = dados[1]
concatenacao_nome_meio = nome_meio[0] + '.'
#print(concatenacao_nome_meio)

concat_nome = dados[2] + ', '+ dados[0] + ' ' + concatenacao_nome_meio
print(concat_nome)

print('*' * 50)
print('Resolução lista 2,segunda opção para resolver a questão a),usando join')

dados = ['Pedro', 'Alvares', 'Cabral']

'''join é usado para concatenar os elementos da lista em uma string'''
nome_completo = ' '.join(dados)

'''Extrair o sobrenome, nesse caso a função slipt esta intriseca'''
nome = dados[0]
sobrenome = dados[-1]

nome_meio = dados[1][0]

'''Formatação da saída de acordo com o que necessito'''

resultado_nome = f'{sobrenome},{nome} {nome_meio}.'

print(resultado_nome)



