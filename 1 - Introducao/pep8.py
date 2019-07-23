"""

import this

The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


A ideia do PEP8 é que possamos escrever códigos python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaço para identação

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco:
- Métodos dentro de uma classe devem ser separados com uma unica linha em branco

[5] - Imports

- Imports devem ser dempre feitos em linhas separadas;
#Import Errado

    import sys, os

#Import Certo

    import sys
    import os

#Não há problemas em utilizar:

from types import StringType, ListType


# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import {
    StringType,
    ListType,
    SetType,
    OutroType
}

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentário ou docstrings e
# antes de constantes ou variaveis globais.

[6] - Espaços em expressões e instruções

#Não Faça:

1 - funcao( algo [ 1 ], { outro: 2 } ),
2 - algo (1)
3 - dict ['chave] = list [indice]
4 - x  = 1
    y    = 3
    variavel_longa   = 5

#Faça

1 - funcao(algo[1], {outro:2})
2 - algo(1)
3 - dict['chave'] = lista[indice]
4 - x = 1
    y =3
    variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this

print('Algo')
