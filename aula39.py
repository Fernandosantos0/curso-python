"""
Iterando strings com while
"""
nome = 'Fernando Santos' # Interáveis
novo_nome = ''

indice = 0
while indice < len(nome):
    novo_nome += f'*{nome[indice]}'
    indice += 1
    
print(novo_nome)