"""Módulo Collections - Counter

Collections -> High-Performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como alor a quantidade
de ocorrências desse elemento."""

# Fazendo o import
from collections import Counter

# Pode se usar qualquer iterável, no exemplo usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 67, 69, 33]

# Exemplo 1
res = Counter(lista) # Utilizando Counter

print(type(res)) # -> <class 'collections.Counter'>
print(res) # -> Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 67: 1, 69: 1, 33: 1})
# Para cada elemento, o Counter criou uma key e atribuiu a quantidade de ocorrencias como value

# Exemplo 2
print(Counter('Faça parte!')) # -> Counter({'a': 3, 'F': 1, 'ç': 1, ' ': 1, 'p': 1, 'r': 1, 't': 1, 'e': 1, '!': 1})

# Exemplo 3

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc id consectetur enim, id molestie tortor. 
Sed nec nisi at risus accumsan ultrices sed at nisi. Suspendisse sed orci eleifend, suscipit massa sed, lobortis 
metus. Nulla ornare sagittis diam, eu blandit quam varius et. Fusce quam turpis, tincidunt nec ornare eget, laoreet 
sodales sapien. Nunc tincidunt est diam, id scelerisque elit sagittis at. Donec quis imperdiet mi. Vivamus ac quam 
posuere, sagittis orci vel, ornare erat. Nulla consectetur orci ac velit dictum, vel luctus felis fringilla. Fusce 
et laoreet sapien."""

palavras = texto.split() # separa as palavras do texto
# print(palavras)
res = Counter(palavras) # conta as palavras
# print(res) 

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5)) # -> [('consectetur', 3), ('id', 3), ('orci', 3), ('ornare', 3), ('sagittis', 3)]