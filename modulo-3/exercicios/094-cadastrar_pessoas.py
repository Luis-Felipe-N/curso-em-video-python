# FAZER UM PROGAMA QUE LEI NOME, SEXO E IDADE DE VÁRIAS PESSAOS E GUARDAR OS DADOS EM UMA LISTA
# NO FINAL MOSTRAR:


pessoas = []
dados = {}
idade = []

while True:
    print('-' * 30)
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))

    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().lower()[0]
    while dados['sexo'] not in 'mf':
        dados['sexo'] = str(input('Sexo [M/F]: '))

    pessoas.append(dados.copy())
    print('-' * 30)

    continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]

    if continuar == 'n':
        break

# QUANTAS PESSOAS FORAM CADASTRADAS 

print('-' * 30)
print(f'-{len(pessoas)} pessoas cadastradas')


# A MÉDIA DE IDADE DO GRUPO

for pessoa in pessoas:
    for chave, valor in pessoa.items():
        if chave == 'idade':
            idade.append(valor)
        # if valor == 'f':
        #     mulher.append(pessoa.copy())


print(f'-A média de idade do grupo é {sum(idade) / len(pessoas):.2f}')


# MULHERES CADASTRADAS 

print('-As mulheres cadastrada foi ', end="")

for pessoa in pessoas:
    if pessoa['sexo'] == 'f':
        for chave, valor in pessoa.items():
            if chave == 'nome':
                print(f'{valor} ', end="")
print()

# UMA LISTA COM TODAS AS PESSOS COM IDADE ACIMA DA MÉDIA

print('Pessoas acima da média: ')
print('-' * 30)
print(f'{"Nome":<10}{"Idade":<10}{"Sexo":<10}')
print('-' * 30)
for pessoa in pessoas:
    if pessoa['idade'] >= 35:
        for keys, values in pessoa.items():
            print(f'{values:<10}', end="")
        print()
print()