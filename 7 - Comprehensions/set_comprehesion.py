# Set Comprehension 

# listas = [1, 2, 3, 4, 5]
# set = {1, 2, 3, 4, 5}

# Exemplos 
numeros = set(num for num in range(1, 6))
print(numeros) # {1, 2, 3, 4, 5}

numeros = {x * 2 for x in range(6)}
print(numeros) # -> {0, 2, 4, 6, 8, 10}

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionario ao invés de set
numeros = {x: x * 2 for x in range(6)}
print(numeros) # -> {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

letras = {letra for letra in 'Geek University'}

print(letras)