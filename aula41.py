""" while/else """
string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra in ' ':
        print('Saído do loop')
        break
    
    print(letra)
    i += 1
else:
    print('O else foi executado')
    print('Não encontrei o espaço na string.')
    
print('Fora do while.')
    