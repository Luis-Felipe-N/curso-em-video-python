# Fazer um radar eletrônico que dará uma multa de 7$ a cada km excedido sendo 80kmh o limite máximo

# Pedi para que o usuário informe qual foi sua velocidade
velocidade = float(input('Qual foi a sua velocidade: '))

# Calcular a multa
multa = (velocidade - 80) * 7

# Mostra se ele está no limite ou terá que pagar alguma multa
if velocidade <= 80:
    print('\033[32mVocê está no limite permitido! Boa viajem!\033[m')
else:
    print(f'\033[31mVocê excedou o limite de velocidade! Sua multa é de {multa}$!\033[m')