# Funções com Parametro Padrão (Default Paramters)

# Funções onde a passagem de parametro seja opcional:
print('Geek Universitary')

print()

# Exemplo de função onde a passagem de parametro é obigatória:
def quadrado(numero):
    return numero ** 2

print(quadrado(3)) # é executado
# -> 9
# print(quadrado()) # retorna um TypeError
# -> TypeError: quadrado() missing 1 required positional argument: 'numero'

# Definindo uma função com valor padrão.


def exponencial(numero, potencia = 2):
    return numero ** potencia
# Obs: Se o usuário passar somente um argumento, este será atribuido ao parametro numero, e será calculado o quadrado
# deste numero

print(exponencial(2, 3)) # Estamos fazendo 2 * 2 * 2
# -> 8
print(exponencial(3, 2)) # Estamos fazendo 3 * 3
# -> 9
print(exponencial(3)) # Por padrão eleva ao quadrado, pois foi definido na criação da função "potencia=2"
# -> 9
print(exponencial(3, 5)) # Eleva a potencia informada pelo usuário
# -> 243



def exponencial2(numero=4, potencia = 2): 
    return numero ** potencia 
# Obs: Se o usuário passar dois argumentos, o primeiro será atribuido ao numero e o segundo ao parametro da potencia.
# Então será realizado o calculo.

print(exponencial2()) # -> 16
print(exponencial2(2, 3)) # -> 8

# Erro
# def teste(num = 2, potencia): # SyntaxError: non-default argument follows default argument
#    return num ** potencia 

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo Instrutor Geek'
    elif nome == 'Geek':
        return 'Pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao()) # -> Pensei que você era o instrutor
print(mostra_informacao(instrutor=True)) # -> Bem-vindo Instrutor Geek
print(mostra_informacao(nome = 'Lucas')) # -> Olá Lucas
print(mostra_informacao(nome = 'Thiago', instrutor=True)) # -> Olá Thiago
print(mostra_informacao('José')) # -> Olá José
print(mostra_informacao(True)) # -> Olá True

# Por quê utilizar parametros com valor default?
# Porque permite que as funções sejam mais flexíveis.
# Porque evita erros com parametros incorretos.
# Nos permite trabalhar com exemplos mais legíveis de código.

# Quais tipos de dados podemos utilizar como valord default para parâmetros?
# - Qualquer tipo de dado.
# - Numeros, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc.

# Exemplo:
def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3)) # 2 + 3
print(mat(2, 2, subtracao)) # 2 - 2

# Escopo - Evitar problemas e confusões...

# Variáveis Globais
instrutor = 'Geek' # variavel global

def diz_oi():
    return f'Oi {instrutor}'


print(diz_oi()) # -> Oi Geek

# Variáveis Locais
def diz_oi2():
    instrutor = 'Python!' # variavel local
    return f'Oi {instrutor}'
# Se tivermos uma variável global, a local terá preferencia.

print(diz_oi2()) # -> Oi Python!


def diz_oi3():
    prof = 'Geek' # variavel local
    return f'Oi {prof}'
# Se tivermos uma variável global, a local terá preferencia.

print(diz_oi3()) # -> Oi Geek
# print(prof) # variavel prof não pode ser chamada globalmente se foi instanciada localmente.
# - >NameError: name 'prof' is not defined

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)
#total = 0 

# def incremente():
#     total = total + 1 # variavel está sendo utilizando em processamento sem ter sido iniciada.
#     return total

# print(incremente()) # retornará um erro.
# -> UnboundLocalError: local variable 'total' referenced before assignment.
total = 0 

def incremente():
    global total # Avisando que queremos utilizar a variavel global.
    
    total = total + 1 # variavel está sendo utilizando em processamento sem ter sido iniciada.
    return total

print(incremente()) # -> 1
print(incremente()) # -> 2
print(incremente()) # -> 3

# Podemos ter funções que são declaradas dentro de funções. Também há uma forma especial de escopo de variável.
def fora():
    contador = 0
    def dentro():
       nonlocal contador
       contador = contador + 1
       return contador
    return dentro()

print(fora()) # -> 1
