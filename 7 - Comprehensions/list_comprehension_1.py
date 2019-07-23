# List Comprehension
# - Utilizando-o, nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension
# [dado for dado in iteravel]

# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res) # -> [10, 20, 30, 40, 50]

# Pra entender melhor o que está acontecendo, devemos dividir a expressão em duas partes, sendo elas:
# A primeira parte: for numero in numeros
# A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res) # -> [0.5, 1.0, 1.5, 2.0, 2.5]

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res) # -> [1, 4, 9, 16, 25]

# List Comprehension vs Loop
# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

# Forma 1
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados) # -> [2, 4, 6, 8, 10]

# Forma 2
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados) # -> [2, 4, 6, 8, 10] 

# Lista Comprehension 
print([numero * 2 for numero in numeros]) # -> [2, 4, 6, 8, 10]

# Outros exemplos
# Exemplo 1
nome = 'Geek University'

print([letra.upper() for letra in nome])
# -> ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']

# Exemplo 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['mayara', 'thiago', 'joão', 'icaro', 'theo', 'lucas']
print([amigo[0].upper() for amigo in amigos]) # -> ['M', 'T', 'J', 'I', 'T', 'L']
print([caixa_alta(amigo) for amigo in amigos]) # -> ['Mayara', 'Thiago', 'João', 'Icaro', 'Theo', 'Lucas']
print([amigo.title() for amigo in amigos]) # -> ['Mayara', 'Thiago', 'João', 'Icaro', 'Theo', 'Lucas']

# Exemplo 3
print([numero * 3 for numero in range(1, 10)]) # -> [3, 6, 9, 12, 15, 18, 21, 24, 27]

# Exemplo 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]]) # -> [False, False, False, True, True, True]

# Exemplo 5
print([str(numero) for numero in [1, 2, 3, 4, 5]]) # -> ['1', '2', '3', '4', '5']