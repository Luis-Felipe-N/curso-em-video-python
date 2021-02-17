# FAZER UM PROGAMA QUE LEIA VÁRIOS NÚMEROS E CADASTRE EM UMA LISTA
# SE O NÚMERO JÁ EXISTI DENTRO DA LISTA, ELE NÃO SERÁ ADICIONADO
# NO FINAL MOSTRE OS VALORES EM ORDEM CRESCENTE

nums = []
while True:
    num = int(input('Digite um número: '))
    if num in nums:
        print('\033[31mA lista já possui esse valor! Não vou adicionar!\033[m')
    else:
        nums.append(num)
        print('\033[32mValor adicionado com sucesso!\033[m')
    con = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    while con not in 'sn':
        con = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if con in 'n':
        break
nums.sort()
print(f'Você digitou os valores {nums}')