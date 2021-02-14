# Ler um nome completo de uma pessoa e mostrar:
nome = input('Digite seu nome completo: ')

# Separar o nome
nome_split = nome.split()

# O nome com todas letras maiúsculas
print(f'Seu nome em maiúsculo fica {nome.upper()}.')

# O nome com todas letras minúsculas
print(f'Seu nome em minúsculo fica {nome.lower()}.')

# Quantas letras ao todo ( sem considera os espaços )
print(f'Seu nome tem {len(nome.replace(" ", ""))} sem os espaços.')

# Quantas letras tem o primeiro nome
print(f'Seu primeiro nome tem {len(nome_split[0])} letras.')