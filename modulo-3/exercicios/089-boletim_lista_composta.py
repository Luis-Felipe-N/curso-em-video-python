# FAZER UM PROGAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS, GUARDANDO TUDO EM UMA LISTA COMPOSTA
# NO FINAL MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRA AS NOTAS INDIVIDUALMENTE

boletim = []
dados = list()
notas =[]

print('-'* 33)
print('{:^33}'.format(' BOLETIM DO ALUNO '))
print('-'* 33)

while True:
    dados.append(str(input('Nome: ')).strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    dados.append(notas[:])
    boletim.append(dados[:])
    notas.clear()
    dados.clear()

    cont = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break

print('{:>2}{:>10}{:>10}'.format('No.', 'Nome', 'Média'))
print('-' * 30)

for e, b in enumerate(boletim):
    print('{:>2}{:>10}{:>10}'.format(e, b[0], sum(b[1]) / 2 ))
print('-' * 30)

while True:
    flag = int(input('Deseja ver nota de qual aluno [999 para parar]: '))
    if flag == 999:
        break
    elif flag > len(boletim):
        print('Digite um aluno válido: ')
    else:
        print(f'Notas de {boletim[flag][0]} são {boletim[flag][1]}')
    print('-' * 30)
print('Progama finalizado...')