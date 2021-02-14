# PEGAR OS 20 COLOCADOS DA TABELA DO BRASILEIRÃO E MOSTRAR:
# APENAS OS 5 PRIMEIROS COLOCADOS 
# OS ÚLTIMOS 4 COLOCADOS 
# UMAS LISTA COM OS TIMES EM ALFABÉTICA
# EM QUE POSIÇÃO ENTÁ O TIME DA CHAPECOENSE
times = 'Internacional', 'Flamengo','Atlético-MG','São Paulo','Fluminense','Grêmio', 'Palmeiras', 'Santos','Corinthians','Bragantino', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo'

ver_tabela = str(input('Quer ver tabela completa [S/N]: ')).strip().upper()[0]
while ver_tabela not in 'SN':
    ver_tabela = str(input('Quer ver tabela completa [S/N]: ')).strip().upper()[0]

if ver_tabela == 'S':
    for colocacao, time in enumerate(times):
        if colocacao < 10:
            print(f'\033[32m{colocacao + 1} - {time}\033[m')
        elif colocacao < 15:
            print(f'\033[33m{colocacao + 1} - {time}\033[m')
        else:
            print(f'\033[31m{colocacao + 1} - {time}\033[m')

print(times[:5])
print(times[-4:])
print(sorted(times))
print('Chapecoense não está na tabela')
# if times[chapecoense] != 'Chapecoense':
#     print('Chapecoense não está na tabela')
# else:
#     print(f'Chapecoense está na {chapecoense}ª posição')

