#  FAZER UM PROGAMA QUE LEIA NÚMEROSINTEIROS DE 0 A 20 E MOSTRE ELE POR EXTENSO

num = int(input('Digite um número entre 0 a 20: '))
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while num < 0 or num > 20:
    num = int(input('\033[31mTENTE NOVAMENTE!\033[m Digite um número válido: '))
print(f'O {num} por extenso é {num_extenso[num]}')