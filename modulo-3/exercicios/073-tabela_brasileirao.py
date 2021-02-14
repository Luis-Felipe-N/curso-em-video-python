times = 'Internacional', 'Flamengo','Atlético-MG','São Paulo','Fluminense','Grêmio', 'Palmeiras', 'Santos','Corinthians','Bragantino', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo'
for colocacao, time in enumerate(times):
    if colocacao < 10:
        print(f'\033[32m{colocacao + 1} - {time}\033[m')
    elif colocacao < 15:
        print(f'\033[33m{colocacao + 1} - {time}\033[m')
    else:
        print(f'\033[31m{colocacao + 1} - {time}\033[m')

