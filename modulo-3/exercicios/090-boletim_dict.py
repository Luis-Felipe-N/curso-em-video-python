pessoas = []
dados = dict()

while True:
    dados['nome'] = str(input('Nome: '))
    dados['media'] = float(input(f'Média de {dados["nome"]}: '))
    if dados['media'] <= 3:
        dados['situacao'] = '\033[31mReprovado\033[m'
    elif dados['media'] <= 6:
        dados['situacao'] = '\033[33mRecuperação\033[m'
    else:
        dados['situacao'] = '\033[32mAprovado\033[m'
    
    pessoas.append(dados.copy())

    continuar = str(input('deseja continuar [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('deseja continuar [S/N]: ')).strip().lower()[0]
    
    if continuar == 'n':
        break


print('-' * 32)
print(f'{"Nome":<10}{"Média":<10}{"Situação":<10}')
print('-' * 32)


for pessoa in pessoas:
    print(f'{pessoa["nome"]:<10}{pessoa["media"]:<10}{pessoa["situacao"]:<10}')
print('-' * 32)