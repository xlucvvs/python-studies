# O *args é um parametro como outro qualquer, isso significa que você poderá chamar de qualquer coisa, desde que co-
# mece com asterisco (*)

# Exemplo
# *xis
# Mas por convenção, a comunidade utiliza *args para defini-lo.

# O que é o args?
# O parametro args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla, então, 
# desde já lembre-se que tuplas são imutáveis.

# Exemplos
def soma_todos_os_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_os_numeros(4, 6, 9))
# Lembrando que caso seja informado uma quantidade de parametros diferente da definida, teremos um erro.
# print(soma_todos_os_numeros(4, 6)) # TypeError

# Entendendo o *args
# Exemplo 1
def soma_todos_os_numeros(*args):
    print(args)

soma_todos_os_numeros() # -> None
soma_todos_os_numeros(1) # -> (1,)
soma_todos_os_numeros(1, 2) # -> (1, 2)

# Exemplo 2
def soma_todos_os_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

# Exemplo 2 - Simplificado
def soma_todos_os_numeros(*args):
    return sum(args)

print(soma_todos_os_numeros()) # -> 0
print(soma_todos_os_numeros(1)) # -> 1
print(soma_todos_os_numeros(1, 2)) # -> 3
# Caso tente passar um valor que não seja numero, será retornado um erro
# print(soma_todos_os_numeros('a')) # -> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Exemplo 3
def soma_todos_os_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_os_numeros('Lucas', 'lucasribeiro.sec@gmail.com', 1, 5, 4, 7)) # -> 17

# Exemplo 4
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de quem você é'

print(verifica_info()) # -> Eu não tenho certeza de quem você é
print(verifica_info(1, True, 'University', 'Geek')) # -> Bem-vindo Geek
print(verifica_info(1, 'University', 3.145, )) # -> Eu não tenho certeza de quem você é

# Exemplo 5 - Tentando passar uma lista
def soma_todos_os_numeros(*args):
    # Se tentarmos passar uma lista, a mesma será considera um unico elemento.
    print(args) # Exemplo: ([1, 2, 3, 4, 5],)
    return sum(args)

numeros = [1, 2, 3, 4, 5]
# Se tentarmos passar uma lista, será retornado um TypeError
# print(soma_todos_os_numeros(numeros)) # -> TypeError: unsupported operand type(s) for +: 'int' and 'list'

# Desempacotador
num1, num2, num3, num4, num5 = numeros
print(soma_todos_os_numeros(num1, num2, num3, num4, num5)) # -> 15

# Desempacotando de forma simplificada.
print(soma_todos_os_numeros(*numeros)) # -> 15
# Obs: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma ele saberá que é necessário desempacotar os dados.
tupla_numeros = (1, 2, 3, 4, 5) # Criando uma tupla
# Passando uma tupla
print(soma_todos_os_numeros(*tupla_numeros)) # -> 15