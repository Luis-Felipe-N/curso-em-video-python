# FAZERR UM PROGAMA QUE GERENCIE O APRIOVEITAMENTO DE UM JOGADOR DE FUTEBOL
# O PROGAMA DEVE LER O NOME DO JOGADOR E QUANTAS PARTIDAS JOGADAS
# DEPOIS LEI A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA 
# NO FINAL GUARDE TUDO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITO DURANTE O COMPEONATO

dados_jogador = dict()
gols_partida = list()

dados_jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
quan_jogos = int(input(f'{dados_jogador["nome"]} jogou qauntas partida: '))

for partida in range(1, quan_jogos + 1):
    gols_partida.append(int(input(f'Quantos gols o {dados_jogador["nome"]} fez na {partida}ª partida: ')))
    
dados_jogador['gols'] = gols_partida[:]
dados_jogador['total'] = sum(gols_partida.copy())
print('*-' * 20)

for chave, valor in dados_jogador.items():
    if chave == 'gols':
        print(f'Os {chave} em cada partida foi {valor}')
    elif chave == 'total':
        print(f'O {chave} de gols foi {valor}')
    else:
        print(f'O {chave} é {valor}')

print('*-' * 20)
print(f'O jogador {dados_jogador["nome"]} participou de {quan_jogos} jogos.')
for partidas, gols in enumerate(dados_jogador['gols']):
    print(f'    =>Na {partidas + 1}ª partida fez {gols}.')
print(f'Tendo um total de {dados_jogador["total"]} jogos')