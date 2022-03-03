# While/Else - Repetição com acumuladores em Python

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador += contador
    contador += 1
else:
    print('Cheguei no Else.')
