# Estruturas Lógicas: and(e), or(ou), not(não), is(é)

# Operadores unários:
#    - not
# Operadores binários:
#    - and, or, is

# Regras de Funcionamento:

# Para o 'and', ambos os valores precisam ser True

ativo = False
logado = True

if ativo and logado:    
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')


# Para o 'or', um ou outro valor precisa ser True

ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')


# Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
# print(not False)

ativo = False
logado = False

if not ativo:
    print('Bem-vindo usuário')
else:
    print('Bem-vindo usuário')


# para o 'is', o valor é comparado com um segundo.

ativo = False
logado = False

if ativo is True:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')

# Ativo é False?
print(ativo is False)

