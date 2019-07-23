# Módulo Collections - Default Dict

# Relembrando dicts
dicionario = {'nome': 'Lucas', 'sobrenome': 'Barros', 'ultimonome':'Ribeiro'}

print(dicionario) # -> {'nome': 'Lucas', 'sobrenome': 'Barros', 'ultimonome': 'Ribeiro'}
print(dicionario['nome']) # -> Lucas
# print(dicionario['outro']) # retorna um KeyError

# Default Dict :)
# Ao criar um dicionário utilizando Default Dict, nós informamos um valor Default, podendo utilizar lambda para 
# isso. Este valor será utilizando sempre que não houver um valor definido. Caso tentemos acessar uma chave que 
# não existe, essa chave será criada e o valor default será atribuido.

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
# Obs: Lambas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
print(dicionario) # - > defaultdict(<function <lambda> at 0x008CA030>, {}) # está vazio

dicionario['nome'] = 'Lucas Barros Ribeiro' 

print(dicionario) # - > defaultdict(<function <lambda> at 0x0133A030>, {'nome': 'Lucas Barros Ribeiro'})
# Se ocorrer a tentativa de passar uma chave que não existe, não será retornando um KeyError
print(dicionario['outro']) # -> 0
# será gerada uma chave 'outro' com valor '0'
print(dicionario) # - > defaultdict(<function <lambda> at 0x02BD95D0>, {'nome': 'Lucas Barros Ribeiro', 'outro': 0})
