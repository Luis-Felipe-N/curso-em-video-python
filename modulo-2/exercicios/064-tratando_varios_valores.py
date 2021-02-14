'''fim = False
cont = n = 0
while not fim:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:# 999 SENDO A CONDIÇÃO DE NÃO CONTA
        fim = True
    elif num < 999:
        n += num
        cont += 1
    else:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m\n Se deseja para digite 999.')
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, n))'''
cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    if num > 999:
        print(print('\033[31mOPÇÃO INVÁLIDA!\033[m\nSe deseja para digite 999.'))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))