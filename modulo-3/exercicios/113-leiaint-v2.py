def leiaint():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            num = 0
        except:
            print(f'\033[31mERRO! Digite um número inteiro vaálido\033[m')
        else:
            return num
            break



def leiafloat():
    while True:
        try:
            num = int(input('digite um número float: '))
        except KeyboardInterrupt:
            num = 0
        except:
            print('\033[31mERRO! Digite um número inteiro vaálido')
        else:
            return num
            break


num_inteiro = leiaint()
num_float = leiafloat()

print(f'O número inteiro digitado foi {num_inteiro} e o float foi {num_float}')