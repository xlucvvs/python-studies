# Módulo Collections - Deque

# Pode-se dizer que o deque é uma lista de alta perfomance.
lista = ['L', 'u', 'c', 'a', 's']
print(lista) # -> ['L', 'u', 'c', 'a', 's']

# Fazendo import
from collections import deque

# Criando deque
deck = deque('Lucas')
print(deck) # -> deque(['L', 'u', 'c', 'a', 's'])

# Adicionando elementos no deque 
deck.append('y') # adiciona no final da lista
print(deck) # -> deque(['L', 'u', 'c', 'a', 's', 'y'])

deck.appendleft('k') # adiciona no começo da lista
print(deck) # -> deque(['k', 'L', 'u', 'c', 'a', 's', 'y'])

# Removendo elementos
print(deck.pop()) # -> y
print(deck) # -> deque(['k', 'L', 'u', 'c', 'a', 's'])
print(deck.popleft()) # -> k
print(deck) # -> deque(['L', 'u', 'c', 'a', 's'])