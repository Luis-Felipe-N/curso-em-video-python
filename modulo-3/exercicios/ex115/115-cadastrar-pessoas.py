import validacao
import models
import os
from time import sleep


def menu():
    print('\033[34m-' * 40)
    print(f'{"CADASTRA PESSOAS":^40}')
    print('-' * 40)
    print('''\033[33m[ 1 ] \033[34m- Ver pesssoas cadastradas\033[m
\033[33m[ 2 ] \033[34m- Cadastrar pesssoas\033[m
\033[33m[ 3 ] \033[34m- Sair do progama''')
    print('-' * 40)
    

while True:
    menu()

    # PEGANDO A OPÇÃO E VÁLIDANDO SE É UM NÚMERO INTEIRO
    op = validacao.leiaint('Sua opção')
    print('-' * 40)
    print('\033[m', end="")
    
    if op == 3:
        break
    elif op == 2:
        while True:
            models.cadastrar()
            op_1 = validacao.leiaSN('Deseja cadastrar outra pessoa [S/N]')
            if op_1 == False:
                break
    elif op == 1:
        models.verPessoas()
    else:
        print(f'\033[31mEssa não é uma opção válida!')
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')