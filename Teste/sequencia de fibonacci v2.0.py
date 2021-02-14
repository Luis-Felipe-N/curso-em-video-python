from time import sleep

print('{:=^80}'.format(' \033[31m SEQUÊNCIA DE FIBONACCI\033[m '))
fim = False
cont = 0
fn = 0
while not fim:
    print('''
\033[34mESCOLHA UMA DAS OPAÇÕES                          
[ 1 ] - MOSTRAR 10 TERMOS
[ 2 ] - ESCOLHER QUANTOS TERMOS
[ 3 ] - EXPLICAÇÃO DO QUE É FIBONACCI
[ 4 ] - MOSTRAR CÓDIGO DE UM PROGAMA DE FIBONACCI
[ \033[31m5\033[m\033[34m ] - FIM DO PROGAMA\033[m
''')
    op = int(input('O que você vai escolher: '))
    if op == 1:
        f1 = 1
        f2 = 1
        cont = 0
        while cont != 10:
            cont += 1
            if cont == 1:
                fn = 0
            elif cont <= 3:
                fn = 1
            else:
                fn = f1 + f2
                f1 = f2
                f2 = fn
            if cont != 10:
                print('\033[32m', fn , '-> ', end='')
            else:
                print(fn, '\033[m')
    elif op == 2:
        f1 = 1
        f2 = 1
        quant = int(input('Quantas vezes: '))
        cont = 0
        while cont != quant:
            cont += 1
            if cont == 1:
                fn = 0
            elif cont <= 3:
                fn = 1
            else:
                fn = f1 + f2
                f1 = f2
                f2 = fn
            if cont != quant:
                print(fn , '-> ', end='')
            else:
                print(fn)
    elif op == 3:
        print('A sequência de fibonacci foi criada por um mateemático chamado \033[31mLeonardo Fibonacci\033[m, e consiste em uma sequência\n de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde \nà soma dos dois anteriores.')
    elif op == 4:
        op_1 = int(input('''
[ 1 ] - CÓDIGO QUE MOSTRA 10 TERMOS
[ 2 ] - USUÁRIO ESCOLHE QUANTOS TERMOS
Qual sua opção: '''))

        if op_1 == 1:
            print('GERANDO CÓDIGO...')
            sleep(2)
            print('''\033[32m
# 1 - CRIE ESSAS VÁRIAVEIS

cont = 0
f1 = 1
f2 = 1

# 2 COLE O CÓDIGO

while cont != 10:
    cont += 1
    if cont == 1:
        fn = 0
    elif cont <= 3:
        fn = 1
    else:
        fn = f1 + f2
        f1 = f2
        f2 = fn
    if cont != 10:
        print(fn , '-> ', end='')
    else:
        print(fn)
            \033[m''')
        elif op_1 == 2:
            print('GERANDO CÓDIGO...')
            sleep(2)
            print('''\033[32m
# 1 - CRIE ESSAS VÁRIAVEIS

f1 = 1
f2 = 1
cont = 0

# 2 - PEÇA A QUANTIDADE DE TERMO PARA O USUÁRIO
quant = int(input('Quantas vezes: '))

# 3 - COLE O CÓDIGO
while cont != quant:
    cont += 1
    if cont == 1:
        fn = 0
    elif cont <= 3:
        fn = 1
    else:
        fn = f1 + f2
        f1 = f2
        f2 = fn
    if cont != quant:
        print(fn , '-> ', end='')
    else:
        print(fn)
        
            \033[m''')
        else:
            print('\033[31mOPÇÃO INVÁLIDA!\033[m')
    elif op == 5:
        fim = True
    else:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
print('\033[32mObrigado e volte sempre!\033[m')
