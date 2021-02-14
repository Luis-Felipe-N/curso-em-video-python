# peça o nome de uma cidade e diz se ela começa ou não com palmas
cidade = input('Digite o nome da cidade: ')
cidade_split = cidade.upper().split()

# Separar a cidade
sn = "PALMAS" in cidade_split[0]

# Mostrar se o usuário mora ou não em uma cidade que começa em Palmas
if sn == True:
    print('Sua cidade começa com Palmas')
else:
    print('Sua cidade não começa com Palmas')
