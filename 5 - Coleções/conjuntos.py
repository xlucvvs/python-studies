# Conjuntos

# - Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
# da matemática.

# Aqui no Python, os conjuntos são chamados de Sets.

# Dito isto, da mesma forma que na matemática:
# - Sets (conjuntos) não possuem valores duplicados;
# - Sets (conjuntos) não possuem valores ordenados;
# - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

# Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos 
# com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

# Os conjuntos (sets) são referenciados em Python com chaves {}

# Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
# - Um dicionário tem chave/valor
# - Um conjunto tem APENAS valor;

# Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado 
# sem gerar erros e não fará parte do conjunto

# Forma 2 - Mais Comum
s = {1, 2, 3, 4, 5, 6, 5}

print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 9 elementos
lista = [99, 2, 34, 23, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 9 elementos
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
# set = {99, 2, 34, 23, 12, 1, 44, 5, 34}
# print(f'Conjunto: {set} com {len(set)} elementos')

# Assim como todo outro conjunto Python, nós podemos colocar tipos de dados misturados em Sets.
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes informaram
# manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python. Já que em uma lista podemos adicionar novos elementos e ter 
# repetição;

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria? Faria um loop na lista...?
# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro, apenas é ignorado
print(s)

# Forma 1
s.remove(3) # Não é índice! Informamos o valor que queremos remover.
# Obs: Caso o valor não exista será retornado um erro (KeyError). Nenhum valor é retornado.
print(s)

# Forma 2
s.discard(4)
# Obs: Caso o valor não exista nenhum erro será retornado.
print(s)

# Copiando um conjunto para outro...
# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(3)
print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
novo.add(3) # Ambos os conjuntos são modificados
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos Matemáticos de Conjuntos
# Imagine que temso dois conjuntos: Um contendo estudantes de curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilheirme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)


# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)


#  Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))