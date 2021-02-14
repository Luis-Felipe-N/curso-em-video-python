# FAZER UM PROGAMA QUE SIMULE UM CAIXA ELETRONICO QUE SOLICITE O VALOR QUE O USUÁRIO DESEJA SACAR
# DEPOIS MOSTRE QUANTAS SEDULAS DE CADA VALOR SERÁ EMITIDO. AS NOTAS SÃO DE 50$, 20$, 10$, 1$
'''
O OPERADOR // DÁ O RESTO DA DIVIÇÃO. ENTÃO SE PEGARMOS COMO EXEMPLO 1234
PRIMEIRO = VERIFICAMOS SE É POSSIVÉL EMITIR UMA NOTA DE 50: 1234 // 50 = 24
COMO JÁ VAMOS EMITIR 24 NOTAS DE 50$ QUE DÁ 1200$.
AGORA TEMOS QUE VERIFICAR SÓ OS 34$ QUE SOBRARAM

SEGUNDO = VERIFICAMOS SE É POSSIVEL EMITIR UMA NOTA DE 20$:  34 // 20 = 1
COMO JÁ VAMOS EMITIR 24 NOTAS DE 50$ E 1 NOTA DE 20$ QUE DÁ 1220$$.
AGORA TEMOS QUE VERIFICAR SÓ OS 14$ QUE SOBRARAM

TERCEIRO = VERIFICAMOS SE É POSSIVEL EMITIR UMA NOTA DE 10$:  14 // 10 = 1
OMO JÁ VAMOS EMITIR 24 NOTAS DE 50$, 1 NOTA DE 20$ E UMA NOTA DE 10$ QUE DÁ 1230.
AGORA TEMOS QUE VERIFICAR SÓ OS 4$ QUE SOBRARAM

QUARTO = VERIFICAMOS QUANTAS NOTA DE 1$ PRECISAMOS EMITIR:  4 // 1 = 1
'''

print('-' * 30)
print('{:^30}'.format('\033[34mBANCO DO LUIS\033[m'))
print('-' * 30)
valor = int(input('Qual valor deseja sacar: R$'))
cont = 0
while True:
    if valor < 0:
        while valor < 0:
            valor = int('Qual valor deseja sacar: R$')
    if valor >= 50:
        print(f'Total de {valor // 50} notas de 50$')
        valor = valor - (valor // 50 * 50)
    if valor >= 20:
        print(f'Total de {valor // 20} notas de 20$')
        valor = valor - (valor // 20 * 20)
    if valor >= 10:
        print(f'Total de {valor // 10} notas de 10$')
        valor = valor - (valor // 10 * 10)
    if valor >= 1:
        print(f'Total de {valor // 1} notas de 1$')
        valor = valor - (valor // 1 * 1)
    if valor == 0:
        break
print('-' * 30)
print('VOLTE SEMPRE!')