"""
Fatiamento de strings
 012345678
 Olá mundo
-987654320
Fatiamento [i:f:p] [::]
Obs.: a função len retornar a qtd
de caracteres da str
"""
variavel = 'Olá mundo'

print(variavel[5])

print(variavel[4:])

print(variavel[4:8])

print(variavel[0:5])

print(variavel[:5])

print(variavel[-8:-2])

print(len(variavel))

print(variavel[0:len(variavel):2])

# Invertendo a string
print(variavel[::-1])

print(variavel[-1:-10:-1])