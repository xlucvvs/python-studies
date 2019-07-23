# Dicionarios

# Em algumas linguagens de programação, os dicionarios python são conhecidos por mapas.
# Isso por que dicionários são coleções do tipo key/value
# key = (0, 1, 2)
# val = (1, 2, 3)

# Dicionários são representados por chaves {}
# print(type({}))


# Criação de Dicionários
# Forma 1 (Mais Comum)
paises = {'br': 'Brasil', 'pt': 'Portugal', 'us': 'Estados Unidos'}
print(paises)
print(type(paises))

# Forma 2 (Menos Comum)
paises = dict(br='Brasil', pt='Portugal', us='Estados Unidos')
print(paises)
print(type(paises))


# Obs: Sobre dicionários:
# - Chave e valor são separados por dois pontos (key:value);
# - Tanto chave quanto valor podem ser de qualquer tipo de dado;
# - Podemos misturar tipos de dados;


# Acessando elementos:
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['pt'])
# Obs: Caso tentemos fazer acesso utilizando uma chave que não existe, teremos um (KeyError)
# Exemplo 1: paises['ca']

# Forma 2 - Acessando via get. (RECOMENDADO)
print(paises.get('br'))
print(paises.get('pt'))


# Obs: Caso tentemos fazer acesso utilizando uma chave que não existe, será retornado um valor (None)
# e não será gerado um (KeyError)
# Exemplo 2: paises.get('ca')
russia = paises.get('ru')

if russia:
    print('Encontrei o país')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão para caso não encontremos o objetivo com a chave informada.
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais}')

print('br' in paises)
print('Portugal' in paises)
print('us' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises[ru]


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário
# como chaves de dicionários.

# Tuplas, por exemplo, são bastante interessante de serem utilizadas como chaves de dicionários, pois, as
# mesmas são imutáveis. 
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))


# Adicionando elementos em um dicionário:
# Forma 1 (Mais Comum)
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

receita['abr'] = 350
print(receita)

# Forma 2 (Menos Comum)
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)


# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas;

# Removendo dados de um dicionário
# Forma 1 (Mais Comum)
ret = receita.pop('mai')
print(ret)
print(receita)

# Obs 1: Aqui é SEMPRE necessário informar a chave, e caso o elemento não seja encontrado, será retornando um (KeyError)
# Obs 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2 (Menos Comum)
del receita['abr']
print(receita)

# Obs1: Caso a chave não exista, será retornado um (KeyError)
# Obs2: Na segunda forma, o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

# Carinho de Compras:
#   Produto 1:
#       - nome
#       - quantidade
#       - preço
#   Produto 2:
#       - nome
#       - quantidade
#       - preço

# 1 - Poderiamos utilizar uma lista para armazenar essas informações.

carrinho = []
produto1 = ['PlayStation 4', 1, 2300.00]
produto2 = ['God Of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Porém, teriamos que saber qual o índice de cada informação no produto.


# 2 - Poderiamos utilizar uma tupla para armazenar essas informações.

produto1 = ('PlayStation 4', 1, 2300.00)
produto2 = ('God Of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Porém, teriamos que saber qual o índice de cada informação no produto.


# 3 - Poderiamos utilizar um dicionário para armazenar essas informações

carrinho = []

produto1 = {'nome': 'PlayStation 4', 'quant': 1, 'preco': 2300.00}
produto2 = {'nome': 'God Of War 4', 'quant': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

d = dict(a=1, b=2, c=3)

# Copiando um dicionário para outro.
# Forma 1 (Deep Copy)
novo = d.copy()

print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d']=4

print(novo)
print(d)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parametros: um iteravel e um valor.
# Ele gera para cada valor do iteravel uma chave e irá atribui-la o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
