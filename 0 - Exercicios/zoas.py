""" 
# Zoas com while

resposta = 'nao'
soma = 0

while resposta != 'sim':
    print('Qual operação você deseja fazer? ')
    operacao = input()

    if operacao == '+':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) + int(valor2)

        print(f'O resultado da soma foi {soma}')

    elif operacao == '-':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) - int(valor2)

        print(f'O resultado da soma foi {soma}')

    elif operacao == '/':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) / int(valor2)

        print(f'O resultado da soma foi {soma}')

    elif operacao == '*':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) * int(valor2)

        print(f'O resultado da soma foi {soma}')

    else:
        print('operacao nao aceita')

    resposta = input('Deseja finalizar? ')
"""
"""
# Zoas com For
resposta = 'sim'
soma = 0

for resposta in 'sim':
    print('Qual operação você deseja fazer? ')
    operacao = input()

    if operacao == '+':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) + int(valor2)

        print(f'O resultado da soma foi {soma}')

    elif operacao == '-':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) - int(valor2)

        print(f'O resultado da soma foi {soma}')

    elif operacao == '/':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) / int(valor2)

        print(f'O resultado da soma foi {soma}')

    elif operacao == '*':
        valor1 = input('Insira o primeiro valor ')
        valor2 = input('Insira o segundo valor ')
        soma = int(valor1) * int(valor2)

        print(f'O resultado da soma foi {soma}')

    else:
        print('operacao nao aceita')

    resposta = input('Deseja finalizar? ')
    if resposta == 'sim':
        break
"""