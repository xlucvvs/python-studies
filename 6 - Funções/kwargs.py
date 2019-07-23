# Entendo o **kwargs

# **xis
# Por convenção, a comunidade utiliza **kwargs para defini-lo.

# Este é só mais um parametro, mas diferente do args que coloca os valores extras em uma tupla, o **kwargs exige
# que utilizemos parametros nomeados e os transforma em um dicionário.

# Exemplo
def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas() # -> {}
cores_favoritas(Marcos='verde', Julia='amarelo', Fernanda='azul', Vanessa='Branco') 
# -> {'Marcos': 'verde', 'Julia': 'amarelo', 'Fernanda': 'azul', 'Vanessa': 'Branco'}

# Exemplo 2
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', Vanessa='branco') 
# -> A cor favorita de Marcos é verde
# -> A cor favorita de Julia é amarelo
# -> A cor favorita de Fernanda é azul
# -> A cor favorita de Vanessa é Branco
cores_favoritas() # ->
cores_favoritas(lucas='azul') # -> A cor favorita de Lucas é azul

# Obs: Ambos os parametros, args e kwargs, não são obrigatórios.

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek"
    return 'Não tenho certeza de quem você é'

print(cumprimento_especial()) # -> Não tenho certeza de quem você é
print(cumprimento_especial(geek='Python')) # -> Você recebeu um cumprimento Pythonico Geek
print(cumprimento_especial(geek='Oi')) # -> Oi geek
print(cumprimento_especial(geek='Especial')) # -> Especial geek

# Nas nossas funções podemos ter, nesta ordem: 
# - Parametros Obrigatórios;
# - *args;
# - Parametros Default (não obrigatórios);
# - **kwargs.

def minha_funcao(num, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {num} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(20, 'Lucas', solteiro=True)
# -> Lucas tem 20 anos
# -> ()
# -> Solteiro
# -> {}

minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
# -> Felicity tem 18 anos
# -> (4, 5, 3)
# -> Solteiro
# -> {}

minha_funcao(34, 'Felipe', eu='não', você='vai')
# -> Felipe tem 34 anos
# -> ()
# -> Casado
# -> {'eu': 'não', 'você': 'vai'}

minha_funcao(19, 'Carla', 9, 4, 3, java='False', python=True)
# -> Carla tem 19 anos
# -> (9, 4, 3)
# -> Casado
# -> {'java': 'False', 'python': True}

# Entendendo porque é importante manter a ordem dos parametros.
# Função com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor=False, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info('a', 'b')) 
# -> ['a', 'b', (), False, {}]
print(mostra_info(1, 2, 3, sobrenome='Barros', cargo='instrutor')) 
# -> a = 1
# -> b = 2
# -> args = (3,)
# -> instrutor = false
# -> kwargs = {'sobrenome': 'Barros', 'cargo': 'instrutor'}

# Redefinindo a função - Função com a ordem incorreta
def mostra_info(a, b, instrutor=False, *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='Barros', cargo='instrutor')) 
# -> a = 1 
# -> b = 2 
# -> args = () 
# -> instrutor = 3 
# -> kwargs = {'sobrenome': 'Barros', 'cargo': 'instrutor'}

# Desempacotar os dados com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} e {kwargs['sobrenome']}"

nomes = {'nome':'Lucas', 'sobrenome':'Barros'}
# Forma Errada
# print(mostra_nomes(nomes)) # -> TypeError: mostra_nomes() takes 0 positional arguments but 1 was given

# Forma Certa
print(mostra_nomes(**nomes)) # -> Lucas e Barros
print(mostra_nomes(nome='João', sobrenome='Vitor')) # -> João e Vitor

def soma_multiplos_numeros(a, b, c):
    print(a+b+c)

soma_multiplos_numeros(5, 6, 4) # -> 15

lista = [1, 2, 3]
soma_multiplos_numeros(*lista) # -> 6

tupla = (1, 2, 4)
soma_multiplos_numeros(*tupla) # -> 7

s = {7, 5, 6}
soma_multiplos_numeros(*s) # -> 18

dicionario = dict(a=1, b=8, c=3)
soma_multiplos_numeros(**dicionario) # -> 12
# Obs: Os nomes das chaves do dicionario devem ser os mesmos dos parametros da função:

# dicio = dict(f=1, g=8, h=3) # definindo chaves que não existem
# soma_multiplos_numeros(**dicio) # imprimindo
# -> TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'f'

# dicio = dict(a=1, b=8, c=3, nome='Geek')
# -> TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'nome'
# dicio = dict(a=1, b=8, c=3)
# soma_multiplos_numeros(**dicio, lang='Python')
# -> TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'lang'

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a+b+c)

dicio = dict(a=1, b=8, c=3, nome='Geek')
# -> 12
soma_multiplos_numeros(**dicio, lang='Python')
# -> 12