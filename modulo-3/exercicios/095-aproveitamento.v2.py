jogadores = []
gols_partida = []
dados_jogador = {}

while True:
    print('-' * 30)
    dados_jogador['nome'] = str(input('Nome: '))
    quan_jogos = int(input(f'Quantos partidas {dados_jogador["nome"]} jogou: '))

    for partida in range(1, quan_jogos + 1):
        gols_partida.append(int(input(f'Quantos gols {dados_jogador["nome"]} fez na {partida}ª partida: ')))

    dados_jogador['gols'] = gols_partida.copy()
    dados_jogador['total'] = sum(gols_partida)
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
    print(f'{e:<4}{jogador["nome"]:<10}{jogador["gols"]}{"":<{12 - len(jogador["gols"]) }}{jogador["total"]}')
    # print(f'{e:<4}')
    # for v in jogador.values():
    #     print(f'{v:<15}')
