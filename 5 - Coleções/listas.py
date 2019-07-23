# Listas

# Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
# de serem DINÂMICAS e podermos colocar QUALQUER tipo de dado.

# Linguagem C/Java: Arrays
#   - Possuem tamanho e tipo de dado fixo;
#   Ou seja, nestas linguagens, se você criar um array de int(inteiros) e com tamanho x, este array
#   será sempre inteiro e poderá ter, SEMPRE, no máximo x valores.

# Em Python:
# - Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando 
# elementos.
# - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, pode-se colocar qualquer tipo de
# dado.

# Listas em Python são representadas por colchetes: []

type([])

lista1 = [1, 3, 12, 18, 6, 9, 53, 54, 1, 25, 44, 56]
# lista1.sort()
# print(lista1)

lista2 = [ 'x', 'l', 'u', 'c', 'v', 'v', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('xlucvvs')

# - Podemos facilmente checar se determinado valor está contido na lista
# num = 8

# if num in lista4:
#     print(f'Encontrei o número {num}')
# else:
#    print(f'Não encontrei o número {num}')

# - Podemos facilmente contar o numero de ocorrências de um valor em uma lista
# print(lista5.count('u'))

# Adicionar elementos em lsitas
# Para adicionar elementos em listas, utilizamos a função append()

# print(lista1)
# lista1.append(42)
# print(lista1)

# lista1.append(42, 53)
# Só é possível adicionar um elemento pro vez.

# lista1.append([42, 53, 8]) # Insere a lista como elemento unico
# print(lista1)

# if [42, 53, 8] in lista1:
#     print('Encontrei a lista')
# else:
#     print('Não encontrei a lista')

# lista1.extend([123, 44, 67]) # Insere cada elemento da lista como valor adicional à lista
# print(lista1)

# lista1.extend(['Geek'])
# print(lista1)

# - Podemos facilmente inserir um novo elemento na lista informando a posição do índice
# lista1.insert(2, 'Novo Valor')
# print(lista1)

# - Podemos facilmente juntar duas listas

# lista6 = lista1 + lista4
# print(lista6)

# lista1.extend(lista4)
# print(lista1)

# - Podemos facilmente inverter uma lista
# Forma 1
# print(lista1)
# print(lista4)

# lista1.reverse()
# lista4.reverse()

# Forma 2
# print(lista1[::-1])
# print(lista4[::-1])

# - Podemos facilmente copiar uma lista
# lista6 = lista4.copy()
# print(lista6)

# Podemos facilmente verificar o tamanho de uma lista
# print(len(lista4))

# Podemos facilmente remover o ultimo elemento de uma lista
# print(lista4)
# lista4.pop()
# print(lista4)

# Podemos remover um elemento pelo indice
# Obs: Os elementos a direita deste indice serão deslocados para a esquerda
# lista4.pop(9)
# print(lista4)

# Podemos remover todos os elementos da lista (zerar)
print(lista4)
lista4.clear()
print(lista4)

# Podemos facilmente repetir elementos em uma lista