# Formatando valores em Python

"""
:s - texto (string)
:d - integer
:f - float
:.(NUMERO)f - quantidade de casas decimais (float)
:(caractere) (> ou < ou ) (quantidade) (tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num = 1
print(f'{num:0>10}') # colocar 0 a esquerda e 10 caracteres, como já tem 1, vai apenas acrescentar 9 zeros

nome = 'Raquel Limâ'
print(f'{nome:#^50}')
# ###################Raquel Limâ####################
