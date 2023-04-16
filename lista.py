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

concatencao_nome = dados[0] + ', ' + dados[2 ] + ' '+ concatenacao_nome_meio
print(concatencao_nome)

print('*' * 50)
print('Resolução lista 2,segunda opção para resolver a questão a),usando join')

dados = ['Pedro', 'Alvares', 'Cabral']

'''join é usado para concatenar os elementos da lista em uma string'''
nome_completo = ' '.join(dados)

'''Extrair o sobrenome, nesse caso a função slipt esta intriseca'''
sobrenome = dados[-1]
nome_meio = dados[1]

'''Formatação da saída de acordo com o que necessito'''

nome_meio_formatado = nome_meio[0] + '.'
resultado_nome = f'{sobrenome},{dados[0]} {nome_meio_formatado}'

print(resultado_nome)



