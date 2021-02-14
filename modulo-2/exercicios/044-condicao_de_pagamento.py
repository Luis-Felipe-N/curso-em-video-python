# Fazer um progama que leia um preço e a condição de pagamento
# - À vista dinheiro/cheque : 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em atè 2x no cartão : preço normal
# - 3x ou mais no cartão : 20% de juros

# Pegando os dados..
print('\033[32m{:=^60}\033[m'.format(' \033[31mLOJA DO LUIS\033[m \033[32m '))
preco = float(input('Preço do produto: R$'))
print('''\033[35mTemos essas formas de pagamento abaixo:
[1] - À vista no dinheiro/cheque
[2] - À vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartâo\033[m''')
forma_de_pagamento = int(input('Forma de pagamento: '))

# Descontos e Juros
v_d_c = preco * 90 / 100
v_c = preco * 95 / 100
c_3x = preco + (preco * 20 / 100)

# Processando a forma de pagamento
if forma_de_pagamento == 1:
    print('\033[32mO VALOR DO PRODUTO É R${}.\nVOLTE SEMPREE!!!\033[m'.format(v_d_c))
elif forma_de_pagamento == 2:
    print('\033[32mO VALOR DO PRODUTO FICOU R${}.\nVOLTE SEMPREE!!!\033[m.'.format(v_c))
elif forma_de_pagamento == 3:
    parcela = preco / 2
    print('O Valor da parcela é de {:.2f}'.format(parcela))
    print('\033[32mO VALOR DO PRODUTO FICOU R${}.\nVOLTE SEMPREE!!!\033[m.'.format(preco))
elif forma_de_pagamento == 4:
    parcelasmaior = int(input('Quantas parcelas: '))
    print('O valor das {} prestações ficou {:.2f}R$.'.format(parcelasmaior,c_3x / parcelasmaior))
    print('\033[32mo VALOR DO PRODUTO FICOU R${}.\nVOLTE SEMPRE!!!\033[m.'.format(c_3x))
else:
    print('\033[31mFORMA DE PAGAMENTO INVÁLIDA!\nTENTE NOVAMENTE MAIS TARDE!\033[m')