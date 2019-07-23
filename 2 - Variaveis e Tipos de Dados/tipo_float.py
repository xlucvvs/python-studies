"""
Tipo Float

Tipo real, decimal

Casas Decimais

Obs: 0 separados de cadas decimais na programação é o ponto e não a virgula.
"""

#Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Tupla
valor = 1, 44, 3, 28, 37
# valor.sort()
print(valor)
print(type(valor))

#Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2, valor3 = 1, 44, 3
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
print(valor3)
print(type(valor3))

# Podemos conveter um float para um int
res = int(valor)
print(res)
print(type(res))

#Podemos trabalhar com numeros complexos
variavel = 7j

