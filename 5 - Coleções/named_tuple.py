# Módulo Collections - Named Tuple

# Recaptulando
tupla = (1, 2, 3)
print(tupla) # -> (1, 2, 3)

# Named Tuple -> São tuplas diferenciadas onde é dado um nome para a mesma e também parâmetros.

# Fazendo Import
from collections import namedtuple

# É preciso definir o nome e parâmetros
# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')
print(cachorro) # -> <class '__main__.cachorro'>

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')
print(cachorro) # -> <class '__main__.cachorro'>

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca',  'nome'])
print(cachorro) # -> <class '__main__.cachorro'>

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray) # -> cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando os dados
# Forma 1
print(ray[0]) # -> idade
print(ray[1]) # -> raca
print(ray[2]) # -> nome

# Forma 2
print(ray.idade) # idade
print(ray.raca) # raca
print(ray.nome) # nome

# Descobrindo o indice do valor
print(ray.index(2)) # Qual o indice desse valor? - > 0
print(ray.count('Chow-Chow')) # Quantas ocorrencias desse valor existe? -> 1