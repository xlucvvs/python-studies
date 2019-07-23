# Funções com Parametro
# - Funções que recebem dados para serem processados dentro da mesma.

# Se pensarmos em um programa, geralmente temos:
# entrada -> processamento -> saída

# Se pensarmos em uma função, já sabemos que temos funções que:
# - Não possuem entrada.
# - Não possuem saída.
# - Possuem entrada, mas não possuem saída.
# - Não possuem entrada, mas possuem saída.
# - Possuem entrada e saída.

# Refatorando uma função:
def quadrado_de_7(): 
    return 7*7

# Passando um parametro para uma função:
def quadrado_de_x(numero): # o parametro é obrigatório, caso não hava, é retornado um (TypeError)
    return numero * numero
    # return numero ** 2 # ela ao quadrado
    # return numero ** 3 # eleva ao cubo

# x = int(input('Insira o numero a ser calculado o quadrado: ')) # <- 3
# resp = quadrado_de_x(x)
# print(resp) # -> 9

# x = int(input('Insira outro numero a ser calculado o quadrado: ')) # -< 4
# print(quadrado_de_x(x)) # -> 16

# Refatorando outra função
def cantar_parabens(aniversiante): 
    print(f'Parabéns pro {aniversiante}!\nNesta data querida.\nMuitas felicidades.\nMuitos anos de vida!')

nome = 'Lucas'
cantar_parabens(nome)
# cantar_parabens() # TypeError: cantar_parabens() missing 1 required positional argument: 'aniversiante'

# Funções podem ter n parametros de entrada, ou seja, podemos receber como entrada em uma função quantos parametros
# forem necessários para a execução do processo. Sendo eles, separados por vírgula.

def calculo(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        return a / b
    elif c == '*':
        return a * b
    else:
        return 'Valor invalido'

res = calculo(2, 5, '*')
print(res)

def outra(num1, b, msg):
    return (num1 + b) * msg

print(outra(1, 3, 'Geek '))
# Obs: Se informamos um número errado de parametros ou argumentos, teremos um TypeError.

# Exemplo:
# resp = calculo(1, 2, '+', 3) # passando argumentos a mais
# -> TypeError: calculo() takes 3 positional arguments but 4 were given

# resp = calculo(1, 2) # passando argumentos a mais
# -> TypeError: calculo() missing 1 required positional argument: 'c'

# Nomeando parametros:
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Lucas', 'Barros Ribeiro'))

# Diferença entre parametros e argumentos:
# Parametros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa!
nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome)) # Se a ordem estiver errada, o valor retornado será errado
# -> Seu nome completo é Jones Felicity

# Argumentos nomeados (KeyWord Arguments)
# Caso utilizemos nomes dos parametros nos argumentos para informá-los, podemos utilizar qualquer ordem.
print(nome_completo(nome='Angelina', sobrenome='Jolie')) # Passando a string
# -> Seu nome completo é Angelina Jolie
print(nome_completo(nome=nome, sobrenome=sobrenome)) # Utilizando variaveis
# -> Seu nome completo é Felicity Jones
print(nome_completo(sobrenome='Barros Ribeiro', nome='Lucas')) # Passando string com keywords em ordem invertida.
# -> Seu nome completo é Lucas Barros Ribeiro

# Erros comuns na utilização do return.
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
            # return / se o return estivesse aqui, o bloco seria finalizado no numero 1, pois não prosseguiria pelos
            # outros valores dentro do for
    return total # a identação é importante, pois o return finaliza o bloco

lista_nums = [1, 2, 3, 4, 5, 6, 7]
tupla_nums = (1, 2, 3, 4, 5, 6, 7)

print(soma_impares(lista_nums)) # utilizando lista
# -> 16
print(soma_impares(tupla_nums)) # utilizando tupla
# -> 16

