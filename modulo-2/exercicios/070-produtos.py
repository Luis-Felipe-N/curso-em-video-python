# FAZER UM PROGAMA QUE LEIA O NOME E PREÇO DE VÁRIOS PRODUTOS E NO FINAL MOSTRE:
# 1 - QUAL É O TOTAL GASTO NA COMPRA 
# 2 - QUANTOS PROUTOS CUSTAM MAIS DE R$1000
# 3 - QUAL É NOME DO PROUTO MAIS BARATO
tot = prod_1000 = cont = valor_barato = nome_barato = 0
print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
while True:
    nome_do_produto = str(input('Nome do produto: '))
    valor_do_produto = float(input('Preço do produto: R$'))
    tot += valor_do_produto
    cont += 1
    if valor_do_produto > 1000:
        prod_1000 += 1 
    if cont == 1:
        valor_barato = valor_do_produto
        nome_barato = nome_do_produto
    elif valor_barato > valor_do_produto:
        valor_barato = valor_do_produto
        nome_barato = nome_do_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'O TOTAL DA COMPRA FOI {tot}')
print(f'{prod_1000} PRODUTOS CUSTAM MAIS DE R$1000')
print(f'O {nome_barato} É O PRODUTO MAIS BARATO E CUSTA {valor_barato}')