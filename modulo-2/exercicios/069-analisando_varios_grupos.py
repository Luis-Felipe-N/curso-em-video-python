# PEDIR IDADE E SEXO DE VÁRIAS PESSOAS E MOSTRAR
# QUANTAS PESSOA TEM MAIS DE 18 ANOS
# QUANTOS HOMENS FORAM CADASTRADO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS

homens = mulher_20 = pessoas_18 = p_cadastrada = 0
while True:
    print('-' * 30)
    print('\033[32mCADASTRE UMA PESSOA\033[m')
    print('-' * 30)
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    p_cadastrada += 1
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    if sexo == 'M':
        homens += 1
    if idade > 18:
        pessoas_18 += 1
    print('-' * 30)
    print(f'\033[34m{p_cadastrada} PESSOAS CADASTRADA\033[m')
    print('-' * 30)
    continuar = str(input('\033[95mDESEJA CONTINUAR? [S/N]: \033[m')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[95mDESEJA CONTINUAR? [S/N]: \033[m')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{pessoas_18} PESSOAS TEM MAIS DE 18 ANOS.')
print(f'{homens} HOMENS FORAM REGISTRADOS.')
print(f'{mulher_20} MULHER TEM MENOS DE 20 ANOS.')