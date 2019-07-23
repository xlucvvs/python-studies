"""
Recebendo dados do Usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre
- Aspas Simples
- Aspas Duplas
- Aspas Simples Triplas
- Aspas Duplas Triplas
Exemplos:
- Aspas Simples -> 'Angelina Jolie'
- Aspas Duplas -> "Angelina Jolie"
- Aspas Simples Triplas -> '''Angelina Jolie'''
"""
# - Aspas Duplas Triplas -> """Angelina Jolie""""""

# Entrada de dados
# print('qual seu nome?')
nome = input('Qual seu nome?')

# Exemplo de print muito antigo 'antigo'
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de print 'antigo'
# print('Seja bem-vindo(a) {0}'.format(nome))
# Exemplo de print moderno
print(f'Seja bem vindo(a) {nome}')

# print('Qual sua idade?')
idade = int(input('Qual sua idade?'))

# Processamento

# Saida
# Exemplo de print muito 'antigo'
# print('%s tem %s anos' % (nome, idade))

# Exemplo de print 'antigo'
# print('A {0} tem {1} anos!'.format(nome, idade))

# Exemplo de print moderno
print(f'{nome} tem {idade} anos')


'''
# int(idade) => cast

Cast é a conversão de um tipo de dado para outro
'''
# print(f'{nome} nasceu em {2019 - int(idade)}')

print(f'{nome} nasceu em {2019 - idade}')
