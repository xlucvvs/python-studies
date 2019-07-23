# Funções com Retorno.

numeros = [1, 2, 3, 4]
print(numeros) # -> [1, 2, 3, 4]
# Podemos armazenar o retorno de uma função em uma variável, quando houver retorno.
ret_pop = numeros.pop() # pop() é uma função, ela remove o ultimo elemento da lista e o retorna.
print(f'Retorno de ret_pop: {ret_pop}') # 4
# Obs: Em Python, quando uma função não retorna nenhum valor. O retorno é 'None'.
ret_pr = print(numeros) # print() é uma função sem retorno
print(f'Retorno de ret_pt: {ret_pr}') # -> None

def quadrado_de_7(): 
    print(7*7) # Imprime o resultado de 7 * 7

ret = quadrado_de_7() # Chama funcao quadrado_de_7 dentro de ret
print(f'Retorno de ret: {ret}')  # Não retorna nada. -> None

# Vamos refatorar essa função, para que ela retorne o valor.
def quadrado_de_7(): 
    return 7*7 # retorna o resultado de 7 * 7
# Funções Python que retornam valores devem retornar estes valores por meio da palavra reservada return.

ret = quadrado_de_7() # Chama funcao quadrado_de_7 de ret
print(f'Retorno de ret: {ret}')  # Imprime a variável que recebeu o retorno de quadrado_de_7 
# -> 49

# Não precisamos necessariamente criar uma variável para receber o retorno de uma função, podemos passar a execução
# para outras funções.
print(f'Retorno da quadrado_de_7 é igual a: {quadrado_de_7() + 1}') # -> 50

# Refatorando a primeira função que foi feita:
def diz_oi(): 
    return 'Oi, ' # retorna 'Oi', antes era impresso 'Oi'

print(diz_oi()) # -> imprime o retorno de diz_oi()

alguem = 'Pedro'
print(diz_oi() + alguem) # Caso a função estivesse imprimindo 'Oi', seria impossível concatenar, pois diz_oi() retor-
# na 'None'

# Obs: Sobre a palavra reservada return:
# return finaliza a função, ou seja, ela sai da execução da função.
# Podemos ter em uma função, diferentes return's
# Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores.

# Forma 1
def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi, '
    print('Estou sendo executado após o retorno') # Essa linha nunca será executada, pois está após o return, ou se-
# ja, após a função ter sido finalizada.
print(diz_oi())

# Forma 2
def nova_funcao():
    variavel = False
    if variavel: # Se variável for True, faça:
        return 4 
    elif variavel is None: # se variável for None, faça:
        return 3.2
    return 'b' # Se variável for False, faça:

print(nova_funcao()) # -> 'b'

# Forma 3
def outra_funcao():
    return 2, 3, 4, 5

print(outra_funcao()) # -> (2, 3, 4, 5)
print(type(outra_funcao())) # - > <class 'tuple'>

# Desempacotando a tupla retornada pela função
num1, num2, num3, num4 = outra_funcao()
print(num1) # -> 2
print(num2) # -> 3
print(num3) # -> 4
print(num4) # -> 5

# Criando uma função para jogar uma moeda, que retornará Cara ou Coroa
from random import random # importamos a biblioteca random

def joga_moeda():
    valor = random() # Gera um número pseudo randomico entre 0 e 1
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização do retorno de uma função, mas que na verdade nem é erro, e sim uma codificação desnes-
# cessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())