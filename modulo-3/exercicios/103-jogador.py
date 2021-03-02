# FUNÇÃO QUE LEIA O NOME E A QUANTIDADE DE GOLS FEITA POR ELE
# SE EM ALGUM CAMPO O VALOR FOR NADA, E PARAMETRO VAI SER O PADRÃO

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


n = str(input('Nome do Jogador: '))
g = str(input('Gols: '))
if g.isnumeric():# VAI VERIFICAR SE É UM NÚMERO
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)