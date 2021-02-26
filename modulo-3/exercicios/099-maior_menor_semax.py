from time import sleep

def maior(lis):
    for e, n in enumerate(lis):
        if e == 0   :
            maiorNumero = n
        elif n > maiorNumero:
            maiorNumero = n
    print(maiorNumero)

lista_de_numeros_maoir = []
quant_num = int(input('Quantos números quer analisar: '))
if quant_num == 0:
    print('~' * 30)
    print('Nenhum número informado!')
else:
    for x in range (1, quant_num + 1):
        lista_de_numeros_maoir.append(int(input(f'{x}ª número: ')))


    print('~' * 30)
    print(f'Analisando os números passados...')
    for n in lista_de_numeros_maoir:
        print(f'{n} ', end="", flush=True)
        sleep(0.5)

    print(f' Foi informado {len(lista_de_numeros_maoir)} números ao todo')
    print('O maior foi ', end="")
    maior(lista_de_numeros_maoir)
