jogadores = []
gols_partida = []
dados_jogador = {}

 
while True:
    print('-' * 34)
    dados_jogador['nome'] = str(input('Nome: ')) # PEGANDO O NOME
    quan_jogos = int(input(f'Quantos partidas {dados_jogador["nome"]} jogou: '))# PEGANDO QUANTIDADE DE PARTIDA JOGADAS

    for partida in range(1, quan_jogos + 1):
        gols_partida.append(int(input(f'    Quantos gols {dados_jogador["nome"]} fez na {partida}ª partida: ')))# PEGANDO GOLS MARCADOS

    dados_jogador['gols'] = gols_partida.copy()# ADICIONANDO GOLS MARCADOS
    dados_jogador['total'] = sum(gols_partida)# ADICIONANDO TOTAL DE GOLS
    gols_partida.clear()
    jogadores.append(dados_jogador.copy())

    continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break

print('-' * 34)
print(f'{"cod":<4}{"Nome":<10}{"gols":<15}{"Total":<5}')
print('-' * 34)

for e, jogador in enumerate(jogadores):
    print(f'{e:<4}{jogador["nome"]:<10}{str(jogador["gols"]):<17}{jogador["total"]:<5}')

print('-' * 34)
while True:
    i = int(input('Qual jogador deseja ver (999 parar):'))
    print('-' * 34)
    if i == 999:
        break
    elif i >= len(jogadores):
        print('\033[31mTente um jogador válido\033[m')
    else:
        print(f'O nome do jogador é {jogadores[i]["nome"]} e seu levantamento foi:')
        for e, v in enumerate(jogadores[i]['gols']):
            print(f'    Na {e + 1}ª partida {jogadores[i]["nome"]} fez {v} gols')
    print('-' * 34)
print('Fim do progama!')