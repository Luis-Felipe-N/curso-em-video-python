from random import randint
# Fazer o computador pensa em um número de 0 a 5 e pedir para que o usuário  tente adivinhar

# Fazer o computador "pensar" em um número de 0 a 5
numero_pensado = randint(0,5)

# Pedindo o número
print('-=-' * 10)
print('{:^30}'.format('Pensando em um número...'))
print('-=-' * 10)
numero_escolhido = int(input('Pensei em um número, tente adivinhar: '))

# Criar um condição de acerto e erro
if numero_pensado == numero_escolhido:
    print('Carambaaaaaa, você é o bichão mesmo em!')
else:
    print(f'Tu é burro em. Pensei no {numero_pensado} e não no {numero_escolhido}')
