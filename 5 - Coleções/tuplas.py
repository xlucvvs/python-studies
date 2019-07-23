# Tuplas (tuples)

# Tuplas são bastante parecidas com listas, existem basicamente duas diferenças:
# 1 - Tuplas são representadas por parenteses (), já as listas por colchetes []
# 2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla, ela não muda.
# Toda operação em uma tupla gera uma nova tupla.

# Cuidado 1: Tuplas são representadas por parentes, mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Ambos códigos acima podem ser utilizados para criar tuplas.

# Cuidado 2: Tuplas com um elemento
tupla3 = (1)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (1, ) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 1,  # Isso é uma tupla
print(tupla5)
print(type(tupla5))

# Podemos concluir que tuplas são definidas pela vírgula(,) e não pelo uso do parenteses().
tupla = (4) # Não é tupla
tupla = (4,) # É tupla
tupla = 4, # É tupla

# Podemos gerar uma tupla dinamicamente com o range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ('Lucas', 'Barros', 'Ribeiro')
nome, sobrenome, ultimonome = tupla

print(nome)
print(sobrenome)
print(ultimonome)

# Obs: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, pois, tuplas são imutáveis.

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * = Se os valores forem inteiros ou reais

tupla = 1, 2, 3, 4, 5

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
# Tuplas são imutáveis, mas podemos sobrescrever seus valores. 

tupla1 = 1, 2, 3
tupla2 = 4, 5, 6

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
tupla1 = tupla1 + tupla2
print(tupla3)
print(tupla1)


# Assim como nas listas, podemos verificar se determinado elemento está contido na tupla.

tupla = 1, 2, 3 

print(3 in tupla)

# Podemos iterar sobre uma tupla

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Podemos contar elementos dentro de uma tupla.

tupla = 'a', 'b', 'c', 'd', 'e', 'a', 'c'

print(tupla.count('c'))

# Vimos em listas
# nome = ('Lucas Barros Ribeiro')
# print(nome)
# print(nome.count('r'))

# Dicas na utilização de tuplas:
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção.

# Exemplo 1
meses = 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
print(meses)

# O acesso a elementos de uma tupla é semelhante ao de listas.
print(meses[1])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i+1

# Verificar em qual indice um elemento está na tupla
print(meses.index('fevereiro'))

# Caso o elemento não exista, será gerado um (ValueError)

# Slicing
# tupla[inicio: fim: passo]

print(meses[4:9])

# Por que utilizar tuplas:
# Tuplas são mais rápidas do que listas
# Tuplas deixam seu código mais seguro. Isso por que trabalhar com elementos imutaveis traz mais segurança
# para o código

# Copiando uma tupla para outra

tupla1 = 1, 2, 3, 4, 5
nova = tupla1 # Na Tupla não temos o problema de Shallow Copy

print(nova)
print(tupla1)

outra = 6, 7, 8, 9, 10
nova = nova + outra

print(nova)
print(tupla1)



