# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1


nome = 'Fernando'

# print(nome[3])
# print(nome[-4])

'''
for letra in nome:
    print(letra)
'''

# Verificar se uma letra esta entre uma palavra
print('a' in nome)
print('z' in nome)
print('ando' in nome)
print('zero' in nome)

print(10 * '-')

print('ndo' not in nome)
print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que desejar encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')