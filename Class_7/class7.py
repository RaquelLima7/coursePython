# Introdução à formatação de Strings

nome = 'Raquel Limâ'
idade = 29
altura = 1.65
e_maior = idade > 18
peso = 40
imc = peso / (altura * altura)

# print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} {idade} anos de idade e seu imc é {imc:.2f}.')
print('{} {} anos de idade e seu imc é {:.2f}.'.format(nome, idade, imc))
