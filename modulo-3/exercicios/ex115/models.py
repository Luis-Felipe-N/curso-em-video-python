import validacao
import os
from time import sleep


def cadastrar():
    with open('dados.txt', 'a') as dados_txt:
            nome = validacao.leiaNome('Nome')
            idade = validacao.leiaint('Idade')
            dados_txt.writelines(f'{nome}:{idade}\n')

    print('\033[32mPESSOA CADASTRADA COM SUCESSO!\033[m')
    sleep(1)

    # LIMPANDO O TERMINAL
    os.system('cls' if os.name == 'nt' else 'clear')


def verPessoas():
    print(f'{"Nome":<30}{"Idade":}')
    print('-' * 40)

    # ABRINDO ARQUIVOS COM PESSOAS CADASTRADAS E MOSTRANDO
    with open('dados.txt','r') as dados_txt:
        for dados in dados_txt:
            dado = dados.split(':')
            print(f'{dado[0]:<30}{dado[1]:}', end="")