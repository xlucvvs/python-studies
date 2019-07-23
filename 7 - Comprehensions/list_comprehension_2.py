# List Comprehension
# Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehensions

# Exemplos

# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares) # -> [2, 4, 6]
print(impares) # -> [1, 3, 5]

# Refatorando
# Qualquer numero par módulo de 2 é 0, e 0 em Python é False, not False = True  
pares = [numero for numero in numeros if not numero % 2]
# Qualquer numero par módulo de 2 é 1, e 1 em Python é True  
impares = [numero for numero in numeros if numero % 2]

print(pares) # -> [2, 4, 6]
print(impares) # -> [1, 3, 5]

# Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

