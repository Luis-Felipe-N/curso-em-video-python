#  FAZER UM PROGAMA QUE LEIA NÚMEROSINTEIROS DE 0 A 20 E MOSTRE ELE POR EXTENSO

num = int(input('Digite um número entre 0 a 20: '))
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = 'S'
while continuar in 'S':
    num = int(input('Digite um número de 0 a 20: '))
    while num < 0 or num > 20:
        num = int(input('\033[31mTENTE NOVAMENTE!\033[m Digite um número 0 a 20: '))
    print(f'O {num} por extenso é {num_extenso[num]}')
    continuar = str(input(('Deseja continuar [S/N]: '))).strip().upper()[0]
    if continuar == 'N':
        break