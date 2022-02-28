# Desafio prático (teste seu conhecimento até aqui)
"""
- Criar variáveis para nome (str), idade (int),
- altura (float) e peso (float) de uma pessoa.
- Criar variável com o ano atual (int)
- Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
- Obter o imc da pessoa com 2 casas decimais (peso e altura da pessoa)
- Exibir um texto com todos os valores na tela usando f-string (com as chaves)
"""
# nome, quantos anos, altura peso
# imc
# ano que nasceu

nome = 'Raquel'
ano_nascimento = 1992
ano_atual = 2021
idade = ano_atual - ano_nascimento
altura = 1.65
peso = 40
imc = peso / (altura * altura)

print(f'Raquel tem {idade} anos de idade, sua altura é {altura} e seu peso é {peso}kg.')
print(f'O IMC da Raquel é {imc:.2f}.')
print(f'Raquel nasceu no ano {ano_nascimento}.')


