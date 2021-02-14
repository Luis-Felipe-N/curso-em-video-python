# FAZER UM PROGAMA QUE LEIA QUALQUER NÚMERO E MOSTRE SEU FATORIAL

# PEDINDO O NÚMERO
num = int(input('Qual número você deseja fatorar: '))
fatorial = 1
fatorando = num
n = 0
lista = []
while n != num:
    n += 1
    fatorial = fatorial * fatorando
    lista.append(fatorando)
    fatorando -= 1
str(lista).strip('[]')
print(f'O número fatorado é {num}! = {"x".join(map(str, lista))} = {fatorial}')