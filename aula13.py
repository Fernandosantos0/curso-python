# IMC = peso / (altura x altura)

nome = 'Fernando'
altura = 1.77
peso = 54
imc = peso / altura ** 2

# Fernando tem 1.77 de altura,
# pesa 54 quilos  seu IMC é 
# ... Ellipsis

"f-strings"
linha_1 = f'{nome} tem {altura: ,.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc: .2f}'

print(linha_1)
print(linha_2)
print(linha_3)