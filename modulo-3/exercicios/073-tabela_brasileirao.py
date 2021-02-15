# PEGAR OS 20 COLOCADOS DA TABELA DO BRASILEIRÃO E MOSTRAR:
# APENAS OS 5 PRIMEIROS COLOCADOS 
# OS ÚLTIMOS 4 COLOCADOS 
# UMAS LISTA COM OS TIMES EM ALFABÉTICA
# EM QUE POSIÇÃO ENTÁ O TIME DA CHAPECOENSE

times = 'Internacional', 'Flamengo','Atlético-MG','São Paulo','Fluminense','Grêmio', 'Palmeiras', 'Santos','Corinthians','Bragantino', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo'
cont = 0 

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
    print('-' * 50)

print(times[:5])
print('-' * 50)
print(times[-4:])
print('-' * 50)
print(sorted(times))
print('-' * 50)
for palavra in times:    
    if palavra == 'Chapecoense':
        cont += 1

if cont == 0:
    print('Chapecoense não está na tabela!')
else:
    print(f'Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')