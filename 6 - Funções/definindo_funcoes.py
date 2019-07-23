# Funções 

# Funções são trechos de código que realizam tarefas específicas, pode ou não receber entradas de dados e retornar 
# uma saida de dados. São muito úteis para executar procedimentos similares por repetidas vezes.

# Obs: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a 
# função seja simplificada.

# Já utilizamos várias funções desde que iniciamos esse curso. Algumas delas:
# - print(); 
# - len(); 
# - max(); 
# - min();
# - count();
# e muitas outras.

# Exemplo de utilização de funções:
cores = ['verde', 'azul', 'preto', 'roxo']

# Utilizando função integrada (Built-In) do Python print()
print(cores) # -> ['verde', 'azul', 'preto', 'roxo']
cores.append('amarelo') # inserindo amarelo na lista de cores
print(cores) # -> ['verde', 'azul', 'preto', 'roxo', 'amarelo']

# E se inserirmos em uma lista que não existe?
# curso.append('mais dados') # 
# print(curso) # retorna um NameError / Erro de atributo
# NameError: name 'curso' is not defined

cores.clear() # zera a lista
print(cores) # -> []

# print(help(print)) # exibe documentação da função print
# DRY - Don't repeat yourself (Não repita a si mesmo)

# Em Python, a forma geral de definir uma função é:

# def nome_da_funcao(parametros de entrada):
#     bloco_da_funcao

# Sendo, nome_da_funcao sempre com letras minusculas e se for nome composto, separado por underline (_ -  SnakeCase)
# parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou
# não.
# bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece,
# neste bloco pode ter ou não retorno da função.

# Obs: Veja que para definir uma função, utilizamos a palavra reservada def, informando ao Python que estamos defi- 
# nindo uma função, também abrimos o bloco de código com o já conhecido dois pontos (:), que é utilizado em python
# para definir blocos.

# Definindo a primeira função:
def diz_oi(): # Essa função não recebe nenhum parametro de entrada.
    print('Oi') # Pode-se usar outras funções dentro de uma função
# Obs: Nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é imprimir Oi.

# Chamada de execução da função.
diz_oi() # certo -> Oi
# diz_oi # errado
# diz_oi () # errado
# Veja que essa função não retorna nada, ela simplesmente executa um print().

# Exemplo 2 
def cantar_parabens(): # Essa função também não recebe nenhum parametro de entrada
    print(f'Parabéns pra você!\nNesta data querida.\nMuitas felicidades.\nMuitos anos de vida!')

cantar_parabens() # Imprime a cantiga de parabéns.

# for n in range(5): # para cada elemento de 1 a 5, faça:
#     cantar_parabens() # Imprime a cantiga de parabéns.

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar essa função através da variável.
canta = cantar_parabens # atribuindo a função a uma variável.
canta() # executa a função cantar_parabens por meio de atribuição da função a uma variável.