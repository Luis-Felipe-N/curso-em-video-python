def leiaint(msg):
    while True:
        try:
            num = int(input(f'{msg}: '))
        except:
            print(f'\033[31mERRO! Digite um número inteiro válido\033[m')
        else:
            return num
            break



def leiafloat():
    while True:
        try:
            num = int(input('Sua opção: '))
        except:
            print('\033[31mERRO! Digite um número inteiro vaálido')
        else:
            return num
            break


def leiaSN(msg):
    op = str(input(f'{msg}: ')).lower().strip()[0]
    while op not in 'sn':
        print('a\033[31mERRO! Essa opção não é válida!\033[m')
        op = str(input(f'{msg}: ')).lower().strip()[0]
    if op == 's':
        return True
    else:
        return False  


def leiaNome(msg):
    while True:
        nome = str(input(f'{msg}: ')).capitalize().strip()
        if nome == '' or nome.isnumeric():
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        else:
            break
    return nome

