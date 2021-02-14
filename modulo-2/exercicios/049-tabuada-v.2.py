from time import sleep
import emoji
# REFAZER A TABUADA, MAS AGORA COM SOMA, MULTIPLIÇÃO, DIVIÇÃO E SUBTRAÇÃO

# MOSTRAR AS OPERAÇÕES PARA O USUÁRIO
print('{:=^40}'.format(' TABUADA V.2 '))
print((emoji.emojize('''
ESCOLHA UM DAS OPÇÃO ABAIXO :backhand_index_pointing_down:''')))
print('''[ 0 ] - ADIÇÃO
[ 1 ] - SUBTRAÇÃO
[ 2 ] - MULTIPLICAÇÃO
[ 3 ] - DIVIÇÃO''')

# PEGANDO A OPERAÇÃO
operacao = int(input('QUAL SUA OPÇÃO: '))
tabuada = int(input('QUAL TABUADA: '))
itens = ['ADIÇÃO', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVIÇÃO']

# BRINCANDO COM LISTA
print(f'GERANDO CALCULADORA DE {itens[operacao]}...')
sleep(2)

# CRIANDO AS CALCULADORAS
for c in range(1, 11):
    if operacao == 0:
        print('{} + {} = {}'.format(tabuada, c, tabuada + c))
    elif operacao == 1:
        print('{} - {} = {}'.format(tabuada, c, tabuada - c))
    elif operacao == 2:
        print('{} * {} = {}'.format(tabuada, c, tabuada * c))
    elif operacao == 3:
        print('{} / {} = {:.1f}'.format(tabuada, c, tabuada / c))