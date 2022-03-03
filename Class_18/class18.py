# While - estrutura de repetição em Python

# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         continue # pula o n° 3
#     print(x)
#     x += 1

# break # finaliza o loop

x = 0 # coluna x:0
while x < 10:
    y = 0 # linha y:0

    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
