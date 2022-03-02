# Índices e fatiamento de strings em Python
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/functions.html

texto = 'Python s2'

nova_string = texto[2:5]
nova_string2 = texto[0::2] # utiliza o : para o step, informar quantos caracteres vai pular
nova_string3 = texto[0:6:2]
print(nova_string)
# tho
print(nova_string2)
# Pto 2
print(nova_string3)
# Pto
