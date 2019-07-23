# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""inteiros = []
i = 0
num = 0

while i < 5:
    try:
        num = int(input('Insira um número inteiro: '))
        if num < 0:
            raise ValueError('Número inserido menor que 0')
    except ValueError as e:
        print('Valor invalido: ', e)
        num = int(input('Insira um número inteiro'))
      
    inteiros.append(num)
    i = i + 1
print(inteiros)"""


# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""reais = []
i = 0
num = 0

while i < 10:
    try:
        num = float(input('Insira um número real: '))
    except:
        print('Valor invalido')
        num = float(input('Insira um número real: '))
    
    reais.append(num)
    i = i + 1

reais.sort()
reais.reverse()
print(reais)"""


# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""notas = []
i = 0
num = 0
media = 0

while i < 4:
    try:
        num = float(input('Insira uma nota: '))
    except:
        print('Valor invalido')
        num = float(input('Insira uma nota: '))
    
    media = media + num
    notas.append(num)
    i = i + 1

media = media / 4

print(f'nota1: {notas[0]}, nota2: {notas[1]}, nota3: {notas[2]}, nota4: {notas[3]}')
print(f'Sua média foi: {media}')"""


# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""vogal = ['a', 'e', 'i', 'o', 'u']
vogais = []
consoantes = []
reais = []
i = 0
num = 0

while i < 10:
    try:
        caractere = input('Insira um caractere: ')
        if caractere in vogal:
            vogais.append(caractere)
        else:
            consoantes.append(caractere)
    except:
        print('Valor invalido')
        caractere = input('Insira um caractere: ')
    
    reais.append(num)
    i = i + 1

print(consoantes)"""


# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e 
# os números IMPARES no vetor impar. Imprima os três vetores.
"""numeros = []
pares = []
impares = []
i = 0

while i < 20:
    try:
        numero = int(input("Insira um numero inteiro: "))
        if numero < 0:
            raise ValueError('Numero inserido menor que 0')
    except ValueError as e:
        print('Valor invalido: ', e)
        numero = int(input("Insira um numero inteiro: "))
    
    numeros.append(numero)

    if (numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)
    i = i + 1

print(f'Os numeros inseridos foram: {numeros}')
print(f'Os numeros pares são {pares}')
print(f'Os impares são {impares}')"""


# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
"""alunos = []

i = 0
while i < 10:

    notas = []
    aluno = []
    
    n = 0
    media = 0
    while n < 4:
        try:
            numero = float(input(f'Insira uma nota do aluno {i+1}: '))
        except:
            print('Valor invalido')
            numero = float(input(f'Insira uma nota do aluno {i+1}: '))
        
        notas.append(numero)

        media = media + notas[n]

        n = n+1

    media = media / 4
    
    aluno.append(notas)
    aluno.append(media)

    alunos.append(aluno)

    i = i+1

i = 0
while i < 10:
    if alunos[i][1] >= 7:
        print(f'Aluno {i}: {alunos[i]}')
    i = i+1"""


# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

"""i = 0
numeros = []
soma = 0
mult = 1

while i < 5:
    try:
        numero = int(input('Insira um numero inteiro: '))
        if numero < 0:
            raise ValueError('Numero inserido menor que 0.')
    except ValueError as e:
        print('Valor inserido invalido: ', e)
        numero = int(input('Insira um numero inteiro: '))
    
    numeros.append(numero)
    soma = soma + numero
    mult = mult * numero

    i = i+1

print(f'Os numeros inseridos foram: {numeros}')
print(f'A soma dos números é igual a: {soma}, a multiplicação dos números é igual a: {mult}')"""


# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

"""i = 0
pessoas = []

while i < 5:
    pessoa = {}
    idade = 0
    altura = 0
    try:
        idade = {'idade':int(input('Insira a idade da pessoa: '))}
        altura = {'altura':float(input('Insira a altura da pessoa: '))}
    except ValueError as e:
        print('Algum dos valores inseridos são invalidos: ', e)

    pessoa.update(idade)
    pessoa.update(altura)
    pessoas.append(pessoa)

    i = i+1

pessoas.reverse()

for pessoa in pessoas:
    print(pessoa)"""


# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
# do vetor.
"""numeros = []
i = 0
soma = 0

while i < 10:
    try:
        numero = int(input('Insira um numero inteiro: '))
        if numero < 0:
            raise ValueError('Número inserido menor que 0')
    except ValueError as e:
        print('Valor inserido invalido: ', e)
    
    numeros.append(numero)

    quadrado = numero * numero
    soma = soma + quadrado
    i = i+1

print(numeros)
print(soma)"""

# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""vetor1 = []
vetor2 = []
vetor3 = []
i = 0

while i < 10:
    elemento1 = input('Insira um valor para o primeiro vetor: ')
    vetor1.append(elemento1)

    elemento2 = input('Insira um valor para o segundo vetor: ')
    vetor2.append(elemento2)

    vetor3.append(elemento1)
    vetor3.append(elemento2)
    
    i = i+1

print(vetor1)
print(vetor2)
print(vetor3)"""


# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
i = 0

while i < 10:
    elemento1 = input('Insira um valor para o primeiro vetor: ')
    vetor1.append(elemento1)

    elemento2 = input('Insira um valor para o segundo vetor: ')
    vetor2.append(elemento2)

    elemento3 = input('Insira um valor para o terceiro vetor: ')
    vetor3.append(elemento3)

    vetor4.append(elemento1)
    vetor4.append(elemento2)
    vetor4.append(elemento3)
    
    i = i+1

print(vetor1)
print(vetor2)
print(vetor3)
print(vetor4)"""


# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 
# 13 anos possuem altura inferior à média de altura desses alunos.

"""i = 0
alunos = []
media = 0

while i < 10:
    aluno = {}
    idade = 0
    altura = 0
    try:
        idade = {'idade':int(input(f'Insira a idade do aluno {i}: '))}
        altura = {'altura':float(input(f'Insira a altura do aluno {i}: '))}
    except ValueError as e:
        print('Algum dos valores inseridos são invalidos: ', e)

    media = media + altura.get('altura')
    aluno.update(idade)
    aluno.update(altura)
    alunos.append(aluno)

    i = i+1

media = media / 10
print(media)

count = 0
i = 0
while i < 10:
    if alunos[i].get('idade') > 13:
        if alunos[i].get('altura') < media:
            count = count + 1
        i = i+1

print(f' A quantidade de alunos com menos de 13 anos e altura inferior a média é: {count}')"""


# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule 
# média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

"""i = 0
ano = [['jan', 0], ['fev', 0], ['mar', 0], ['abr', 0], ['mai', 0], ['jun', 0], ['jul', 0], ['ago', 0], ['set', 0], 
['out', 0], ['nov', 0], ['dez', 0]]
media = 0

while i < 12:
    try:
        ano[i][1] = float(input(f'Insira a temperatura do mês "{ano[i][0]}": '))
    except ValueError as e:
        print('Algum dos valores inseridos são invalidos: ', e)
    media = media + ano[i][1]
    i = i+1

media = media / 12
print(media)

acima = []

i = 0
z = 0
while i < 12:
    if ano[i][1] > media:
        acima.insert(z, ano[i])
        z = z+1
    i = i+1

print(acima)"""


# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia para a vítima?"
# - "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
# "Assassino". Caso contrário, ele será classificado como "Inocente".

"""cont = 0
lista = []
resposta = ''

resposta = input('Você telefonou para a vítima?')
lista.append(resposta)

resposta = input('Você esteve no local do crime?')
lista.append(resposta)

resposta = input('Você mora perto da vítima?')
lista.append(resposta)

resposta = input('Você devia para a vítima?')
lista.append(resposta)

resposta = input('Você já trabalhou com a vítima?')
lista.append(resposta)

cont = lista.count('sim')
    
if cont == 1:
    print('Você não é suspeito')
elif cont == 2:
    print('Você é suspeito')
elif cont > 2 and cont < 5:
    print('Você é cumplice')
elif cont == 5:
    print('Você é o assassino')"""


# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de 
# dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
"""i = 0
lista = []

soma = 0

while i != -1:
    valor = float(input("Insira uma nota: "))
    if valor != -1:
        soma = soma + valor
        lista.append(valor)
    if valor == -1:
        break

print(lista)
normal = lista

lista.reverse()

reverso = lista

for n in reverso:
    print(n)

print(soma)

media = soma / len(normal)
print(media)

for n in normal:
    if n > media:
        print(n)

for n in normal:
    if n < 7:
        print(n)

print('Fim do programa')"""


# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor 
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos 
# seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será 
# determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco 
# distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
# O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme 
# o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

"""story = []

nome = input('Digite o nome do atleta: ')
story.append(nome)

while nome != '':
    salto = 0
    cont = 1
    i = 0
    media = 0
    while i < 5:
        try:
            salto = float(input(f'Insira a distancia do {cont} salto: '))
            cont = cont + 1
            media = media + salto
            if salto < 0:
                raise ValueError('Número inserido menor que 0')
        except ValueError as e:
            print('O valor inserido é invalido: ', e)

        story.append(salto)
        i = i +1
    
    media = media / 5
    story.append(media)

    print('Atleta:', story[0])
    print('Saltos:', story[1:6])
    print('Média:', story[6])
    
    nome = input('Insira o nome do atleta: ')
    if nome != '':
        i = 0
        story.clear()
        story.append(nome)
    else:
        break"""


# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jo- 
# gador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas tele-
# fonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a lin-
# guagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente
# ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. e um número 
# inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro 
# número. Após o final da votação, o programa deverá exibir:
# - O total de votos computados;
# - Os números e respectivos votos de todos os jogadores que receberam votos;
# - O percentual de votos de cada um destes jogadores;
# - O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual
# de votos dados a ele.

# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pe-
# lo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de 
# cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total
# de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O dispo-
# sição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada exe-
# cução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo
# texto no disco, obedecendo a mesma disposição apresentada na tela. Enquete: Quem foi o melhor jogador?

"""i = 1
votos = []
votacao = []

while i != 0:
    try:
        jogador = int(input('Insira o numero do jogador: '))
        if jogador < 0:
            raise ValueError('O número digitado é menor que 0')
        elif jogador == 0:
            break
        elif jogador < 24:
            votos.append(jogador)
        else:
            raise ValueError('O número digitado não coresponde a nenhum jogador')
    except ValueError as e:
        print('O número digitado é inválido:', e)
    
votos.sort()
print('O total de votos computados foi:', len(votos))

z = 1
melhor = votos.count(1)

while z < 24:
    percent = (votos.count(z) * 100 ) / len(votos)
    print(f'Jogador {z} teve {votos.count(z)} votos, correspondentes a {percent}%')

    if z > 1:
        if melhor < votos.count(z):
            melhor = votos.count(z)
        else:
            melhor = melhor
    z = z + 1

print('')
print(f'O melhor jogador foi o {melhor}')"""

# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de 
# organizações: "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da 
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão 
# ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
# armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual 
# de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o 
# seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

# i = 1

# print("""Qual o melhor Sistema Operacional para uso em servidores?
"""1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS"""
# 6- Outro """)

"""votos = []
votacao = []

while i != 0:
    try:
        voto = int(input('Digite o numero correspondente a opção desejada: '))
        if voto < 0:
            raise ValueError('Número digitado menor que zero')
        elif voto == 0:
            break
        if voto > 6:
            raise ValueError('Número digitado não corresponde a nenhuma opção')
        else:
            votos.append(voto)
    except ValueError as e:
        print('Valor inserido é considerado inválido: ', e)

votos.sort()

z = 1
while z < 7:
    percent = (votos.count(z) * 100 ) / len(votos)

    votacao.append([z, votos.count(z), percent])
    print(votacao)
    z = z + 1
"""
# print(f"""
"""Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server            {votos.count(1)}     {votacao[0][2]} 
Unix                      {votos.count(2)}     {votacao[1][2]} 
Linux                     {votos.count(3)}     {votacao[2][2]} 
Netware                   {votos.count(4)}     {votacao[3][2]} 
Mac OS                    {votos.count(5)}     {votacao[4][2]} 
Outro                     {votos.count(6)}     {votacao[5][2]} 
-------------------     -----
Total                    {len(votos)}"""
# """)

# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcança-
# do durante o ano que passou. Para isto, contratou você para desenvolver a aplicação que servirá como uma projeção 
# de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria fi-
# nanceira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

# a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
# a. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor 
# mínimo; 

# Neste momento, não se  deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos
# ou outras particularidades. 

# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor 
# de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o 
# valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá 
# apresentar:
# - O salário de cada funcionário, juntamente com o valor do abono;
# - O número total de funcionário processados;
# - O valor total a ser gasto com o pagamento do abono;
# - O número de funcionário que receberá o valor mínimo de 100 reais;
# - O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. 
# - Os valores podem mudar a cada execução do programa.

# Projeção de Gastos com Abono
# ============================ 
 
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0
 
# Salário    - Abono     
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00
 
# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00

"""funcionarios = []
salario = 1
i = 1
maior = 0

while salario != 0:
    funcionario = []
    funcionario.append(i)
    try:
        salario = float(input('Insira o valor do salário: '))
        if salario < 0:
            raise ValueError("Valor informado é menor que 0")
        elif salario > 500:
            abono = (salario * 20) / 100
            funcionario.append(salario)
            funcionario.append(abono)
            if maior < abono:
                maior = abono
            else:
                maior = maior
        else:
            abono = 100
            funcionario.append(salario)
            funcionario.append(abono)
            if maior < abono:
                maior = abono
            else:
                maior = maior
    except ValueError as e:
        print('Valor inserido é invalido: ', e)

    funcionarios.append(funcionario)
    i = i + 1

i = 1
gastos_abono = 0
cont_min_abono =0
z = 0
print('Funcionário    Salário      Abono')

while i < len(funcionarios):
    print(f'     {i}         R${funcionarios[(i-1)][1]}      R${funcionarios[(i-1)][2]}')
    gastos_abono = gastos_abono + funcionarios[(i-1)][2]
    if funcionarios[(i-1)][2] == 100:
        cont_min_abono = cont_min_abono + 1
    i = i + 1

print(f'Foram processados {len(funcionarios)} colaboradores')
print(f'Total gasto com abonos: R${gastos_abono}')
print(f'Valor mínimo pago a {cont_min_abono} colaboradores')
print(f'Maior valor de abono pago: R${maior}')"""


# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um 
# litro de combustível. Calcule e mostre:
# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilô-
# metros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exem-
# plo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar
# a cada execução do programa.

# Comparativo de Consumo de Combustível
# Veículo 1
#Nome: fusca, Km por litro: 7

#Veículo 2
# Nome: gol, Km por litro: 10

# Veículo 3
# Nome: uno, Km por litro: 12.5

# Veículo 4
# Nome: Vectra, Km por litro: 9

# Veículo 5
# Nome: Peugeout, Km por litro: 14.5

# Relatório Final
# 1 - Fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - Gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - Uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - Vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - Peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

"""i = 1 

veiculos = []
menor_consumo = [float(0)]
preco_gasolina = float(input('Qual o preço da gasolina atualmente?'))

while i < 6:
    veiculo = []
    nome = input('Insira o nome do veículo: ')
    veiculo.append(nome)
    try:
        consumo = float(input(f'Quantos KM o {nome} faz com 1 litro?'))
        if consumo < 0:
            raise ValueError('Valor informado invalido')
        else:
            veiculo.append(consumo)
            if consumo > menor_consumo[0]:
                menor_consumo.pop()
                menor_consumo.append(consumo)
            else:
                print('')
    except ValueError as e:
        print('Valor inserido invalido: ', e)

    litros = 1000 / consumo
    veiculo.append(litros)
    gasto = litros * preco_gasolina
    veiculo.append(gasto)

    veiculos.append(veiculo)

    i = i +1

print(veiculos)
z = 1
print('Relatório Final')
while z < 6:
    print(f'{z} - {veiculos[(z-1)][0]} - {veiculos[(z-1)][1]} - {veiculos[(z-1)][2]} litros - R${veiculos[(z-1)][3]}  ')
    z = z+1

# z = 1
# while z < 6:
#     if menor_consumo[0] == veiculos[(z-1)][1]:
#         print(f'o menor consumo é do {veiculos[(z-1)][0]}')
#     z = z + 1

# Outra forma de fazer:
for n in veiculos:
    if menor_consumo[0] == n[1]:
        print(n[0])"""
    


# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer 
# um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses 
# que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um 
# número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# - necessita da esfera;
# - necessita de limpeza; 
# - necessita troca do cabo ou conector; 
# - quebrado ou inutilizado Uma identificação igual a 
# zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1 - necessita da esfera                  40                     40%
# 2 - necessita de limpeza                 30                     30%
# 3 - necessita troca do cabo ou conector  15                     15%
# 4 - quebrado ou inutilizado              15                     15%

defeito = 1
mouses = []

while defeito != 0:
    mouse = []
    id = int(input('Insira o numero de identificação do mouse: '))
    try:
        print('1 - necessita da esfera')
        print('2 - necessita de limpeza')
        print('3 - necessita troca do cabo ou conector')
        print('4 - quebrado ou inutilizado Uma identificação igual a')
        defeito = int(input('Insira a situação do mouse: '))
        if defeito < 0:
            raise ValueError('Número inserido menor que 0')
        elif defeito == 0:
            break
        else: 
            mouse.append(id)
            mouse.append(defeito)
            mouses.append(mouse)
    except ValueError as e:
        print('Valor informado é invalido', e)

print('Situação                             Quantidade              Percentual')
print(f'1 - necessita da esfera                  40                     40%')
print(f'2 - necessita de limpeza                 30                     30%')
print(f'3 - necessita troca do cabo ou conector  15                     15%')
print(f'4 - quebrado ou inutilizado              15                     15%')

for m in mouses:
    mouses.count()m[2]



"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e 
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar 
o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de 
forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá 
ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso 
também deverá ser feito através de uma função, que será chamada pelo programa principal.
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. 
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para 
gerar numeros aleatórios, simulando os lançamentos dos dados.
"""