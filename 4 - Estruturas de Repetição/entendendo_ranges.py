# Ranges

# - Precisamos conhecer o loop for para usar os ranges
# - Precisamos conhecer o range para trabalhar melhor loops

# Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
# mas sim de maneira especificada.

# Formais Gerais:

# Forma 1
# range(valor_de_parada)
# Obs: Valor de parada não incluso. (Inicia com indice 0 e passado de 1 em 1).

# Exemplo Forma 1
# for num in range(11):
#     print(num)

# Forma 2
# range(valor_de_inicio, valor_de_parada
# Obs: Valor de parada não incluso(Inicia com o indice inserido pelo usuario e passa de 1 em 1).

# Exemplo Forma 2
# for num in range(4, 11):
#     print(num)

# Forma 3
# range(valor_de_inicio, valor_de_parada, passo)
# Obs: Valor de parada não incluso(Inicia com o indice passado pelo usuario e passa de x em x, sendo x um valor
# inserido pelo usuario).

# Exemplo Forma 3
# for num in range(5, 100, 5):
#     print(num)

# Forma 4 (Inversa)
# range(valor_de_inicio, valor_de_parada, passo)
# Obs: Valor de parada não incluso(Inicia com o indice passado pelo usuario e passa de x em x, sendo x um valor
# inserido pelo usuario).

# Exemplo Forma 4
# for num in range(10, 0, -1):
#     print(num)