# Operadores lógicos + IF/ELIF/ELSE

# and, or, not
# in, not_in

nome = 'Raquel'

if 'u' in nome:
    print('Existe a letra U no seu nome.')

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_bd = 'raquellima7'
senha_db = '123456'

if usuario == usuario_bd and senha == senha_db:
    print('Você está logado no sistema.')
else:
    print('Você não está logado no sistema.')