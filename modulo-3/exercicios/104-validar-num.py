# FAZER UMA FUNÇÃO QUE VÁLIDE SE O QUUE FOI DIGITADO É OU NÃO UM NÚMERO

def leiaInt(num=''):
    while True:
        num = str(input('Digite um número: '))
        e_num = False
        for p in num.lower():
            if p == '':
                print('\033[31mERRO! TENTE NOVAMENTE!\033[m')
                break
            elif p in 'abcdefghijklmnopqrstuvwxyz':
                print('\033[31mERRO! TENTE NOVAMENTE!\033[m')
                break
            else:
                e_num = True

        if e_num:
            print(f'Você digitou {num}')
            break


leiaInt()