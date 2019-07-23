# Loop For

# Loop -> é uma estrutura de repetição
# Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

# Exemplos de iteráveis:
# - String
#     nome = 'Geek University'

# - Listas
#     lista = [1, 3, 5, 7, 9]

# - Range
#     numeros = range(1,10)

# 1 - For

nome = 'Geek University'

# Exemplo de For 1 (Iterando sobre uma string)
# for letra in nome:
#     print(letra)

numeros = range(1, 10)  # Temos que transformar em uma lista
lista = [1, 3, 5, 7, 9]

# Exemplo de For 2 (Iterando sobre uma lsita)
# for numero in lista:
#     print(numero)

# Exemplo de For 3 (Iterando sobre um range)
# for numero in range(1, 10):
#     print(numero)

# range (valor_inicial, valor_final)
# Obs: O valor final não é incluso

# For em C ou Java:

# for (int i = 0: i < limitador; i++) {
#     ~execução do loop~
# }

# Python
# for item in interavel:
#     ~execução do loop~

# Enumerate:

# ((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

# for indice, letra in enumerate(nome):
#     print(nome[indice])

# for indice, letra in enumerate(nome):
#     print(letra)

# for _, letra in enumerate(nome):
#     print(letra)

# Obs: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

# for valor in enumerate(nome):
#     print(valor)
#     print(type(valor))

# qtd = int(input('Quantas vezes esse loop deve rodar?'))
# soma = 0

# for n in range(1, qtd+1):
#     print(f'Imprimindo {n}')

# for n in range(1, qtd+1):
#     num = int(input(f'Informe o {n}/{qtd} valor: '))
#     soma = soma + num
# print(f'A soma é {soma}')

nome = 'Geek '

# for letra in nome:
#     print(letra)

# for letra in nome:
#     print(letra, end=' ')

# print(nome * 3)

# Tabela de Emojis Unicode: http://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print('\U0001F60D' * num)
