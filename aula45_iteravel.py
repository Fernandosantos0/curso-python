""" 
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Luiz'.__iter__()
texto2 = iter('Fernando') # __iter__()

# print(texto2)

# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())
# print(texto2.__next__())

# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))

# numeros = range(0, 100, 8)
# for numero in numeros:
#     print(numero)

texto3 = 'Luiz' # iterável
iterador = iter(texto3) # iterator ou interador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
    

# for letra in texto3:
#     print(letra)