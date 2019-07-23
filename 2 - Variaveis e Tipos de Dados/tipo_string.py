"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre àspas simples -> 'Uma string', '234', 'a', 'True, '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

"""
# [ 0,   1,   2,   3,   4,   5,   6 ]
# ['x', 'l', 'u', 'c', 'v', 'v', 's']

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13, 14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't','y']

geek = 'Geek University'

print(geek[::-1])  # Inversão da String Pythônico
# -- ytisrevinU keeG
print(geek.replace('G', 'W'))
# -- Week University
print(geek.replace('e', 'i'))
# -- Giik Univirsity

print(type(geek))

geek = 'xlucvvs'
print(geek)
print(type(geek))

geek = "xlucvvs"
print(geek)
print(type(geek))

geek = "xlucvv's"
print(geek)
print(type(geek))

geek = 'xluc \nvvs'
print(geek)
print(type(geek))

geek = 'Xluc \' VVS'
print(geek)
print(type(geek))

geek = 'xlucvvs'
print(geek.upper())
# -- XLUCVVS

geek = 'XLUCVVS'
print(geek.lower())
# -- xlucvvs

geek = 'XLUC VVS'
print(geek.split())
# -- ['XLUCV', 'VVS'] #Transforma em uma lista de strings

geek = 'xlucvvs'
print(geek[1:4])  # Slice de string

print(geek[0:7])  # Slice de string

geek = "luc geek"
print(geek.split())
# -- ['luc', 'geek']
print(geek.split()[0])
# -- luc
print(geek.split()[1])
# -- geek

texto = 'socorram me subino onibus em marrocos'  # Palindromo
print(texto)
# -- socorram me subino onibus em marrocos
print(texto[::-1])
# -- socorram me subino onibus em marrocos

ave = 'arara'  # Palindromo
print(ave)
# -- arara
print(ave[::-1])
# -- arara
"""