# len - Quantidade de caracteres

usuario = input('Nome de usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Precisa de de pelo mesnos 6 caracteres.')
else:
    print('Vocẽ foi cadastrado no sistema')
    