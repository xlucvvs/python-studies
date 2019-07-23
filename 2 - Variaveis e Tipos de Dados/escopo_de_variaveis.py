"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis Globais
   - Variáveis Globais são reconhecidas, ou seja, seu escopo compreende todo o programa.
2 - Variáveis Locais
   - Variáveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
   está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos uma variável nós
não colocamos o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Em Java:
int numero = 42;

Em Python:
numero = 42

numero = 42
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10
    print(novo)
# -- 52
"""
