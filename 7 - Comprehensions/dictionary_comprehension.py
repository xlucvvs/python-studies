# Dictionary Comprehension

# Pense no seguinte:

# Se quisermos criar uma lista fazemos:
# lista = [1, 2, 3, 4]

# Se quisermos criar uma tupla:
# tupla = (1, 2, 3, 4) ou simplesmente, tupla = 1, 2, 3, 4

# Se quisermos criar um set:
# conjunto = {1, 2, 3, 4}

# Se quisermos criar um dicionário:
# dicionario = {'a':1, 'b':2, 'c':3, 'd':4}

# Sintaxe 
# {chave:valor for valor in interavel} # Dictionary Comprehension
# [valor for valor in interavel] # List Comprehension

# Exemplos 

numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(numeros)
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numeros2 = [1, 2, 3, 4] # ou
numeros2 = (1, 2, 3, 4) # ou
numeros2 = {1, 2, 3, 4}

print(numeros2) # -> [1, 2, 3, 4]
quadrado2 = {valor: valor **2 for valor in numeros2}
print(quadrado2) # -> {1: 1, 2: 4, 3: 9, 4: 16}

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura) # -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Exemplo com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res) # -> {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}