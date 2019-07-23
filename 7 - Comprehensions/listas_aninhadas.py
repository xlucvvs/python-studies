# Listas aninhadas
# - Algumas linguagens de programção (C/Java) possuem uma estrutura de dados chamados de arrays: 
#   - Unidimensionais (Arrays/Vetores);
#   - Multidimensionais (Matrizes);

#   Em Python nós temos as Listas
#   numeros = [1, 'b', 3.234, True, 5]

# Exemplos
listas = [[1, 2, 3],[4, 5, 6], [7, 8, 9]] # 3 x 3

print(listas) # -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(listas)) # -> <class 'list'>

# Acessando os Dados
print(listas[0]) # -> [1, 2, 3]
print(listas[1]) # -> [4, 5, 6]
print(listas[2]) # -> [7, 8, 9]
print(listas[0][1]) # -> 2
print(listas[1][0]) # -> 4
print(listas[1][-1]) # -> 6
print(listas[2][-2]) # -> 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    print(lista) # imprime cada uma das listas

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos 
# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

# Gerando valores iniciais 
print([['*' for i in range(1,4)] for j in range(1,4)])