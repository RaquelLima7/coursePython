# Documentação e funções built-in úteis

# https://docs.python.org/3/library/stdtypes.html
# https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

# isdecimal(), isdigit(), isnumeric()

# num e positivos
# print(num_1.isnumeric())
# print(num_2.isnumeric())

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
else:
    print('Digite um número válido.')
