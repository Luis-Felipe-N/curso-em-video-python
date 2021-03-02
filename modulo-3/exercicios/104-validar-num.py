# FAZER UMA FUNÇÃO QUE VÁLIDE SE O QUUE FOI DIGITADO É OU NÃO UM NÚMERO

def leiaInt(num=''):
    while True:
        num = str(input('Digite um número: ')).strip()
        if num.isnumeric():
            break
        else:
            print('\033[31mDigite um número válido!\033[m')
    return num

n = leiaInt()
print(f'Você digitou o número {n}')
