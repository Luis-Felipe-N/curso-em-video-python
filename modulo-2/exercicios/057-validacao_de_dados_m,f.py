# FAZER UM PROGAMA QUE LEIA O SEXO DE UMA PESSOA E SSÓ ACEITE M, F.
'''n = 1
while n == 1:
    sexo = str(input('Sexo [M\F]: ')).upper()
    if sexo in 'MF':
        n = 0
        if sexo == 'M':
            sexo_escolhido = 'masculino'
        else:
            sexo_escolhido = 'femino'
    else:
        print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
print(f'Você é do sexo {sexo_escolhido}.')'''
lista_erro_f = ['MOCA', 'MOÇA', 'MENINA', 'MULHER']
lista_erro_m = ['HOMEM', 'OMEN', 'MENINO', 'MOCO', 'MOÇO', 'MACHO']
sexo = str(input('SEXO [M\F]: ')).strip().upper()
if sexo in lista_erro_f:
    sexo = 'F'
elif sexo in lista_erro_m:
    sexo = 'M'

while sexo not in 'MF':
    sexo = str(input('SEXO INVÁLIDO, POR FAVOR, INSIRA UM SEXO VÁLIDO [M\F]: ')).strip().upper()
    if sexo in lista_erro_f:
        sexo = 'F'
    elif sexo in lista_erro_m:
        sexo = 'M'
print(f'SEXO {sexo} REGISTRADO COM SUCESSO!')