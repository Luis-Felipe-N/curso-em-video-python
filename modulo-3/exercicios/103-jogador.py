# FUNÇÃO QUE LEIA O NOME E A QUANTIDADE DE GOLS FEITA POR ELE
# SE EM ALGUM CAMPO O VALOR FOR NADA, E PARAMETRO VAI SER O PADRÃO

def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


nome = str(input('Nome do Jogador: '))
gols = str(input('Gols: '))
if nome == '' and gols == '':
    jogador()
elif gols == '':
    jogador(nome=nome)
elif nome == '':
    jogador(gols=gols)