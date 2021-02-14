# Pedi o nome completo de uma pessoa e mostra o primeiro e o ultimo nome
nome_completo = str(input('Digite seu nome completo: ')).strip()

# Dividir o nome em partes
nome_completo = nome_completo.split()

# Mostrar o primeiro e ultimo nome
print(f'Primeiro: {nome_completo[0]}')
print(f'Ultimo: {nome_completo[-1]}')